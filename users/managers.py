from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Oddiy foydalanuvchini yaratish.
        """
        if not email:
            raise ValueError("Email manzili kiritilishi shart!")
        if not username:
            raise ValueError("Username kiritilishi shart!")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Superuser yaratish.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True) 
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser is_staff=True bo‘lishi kerak!")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser is_superuser=True bo‘lishi kerak!")
        
        return self.create_user(email, username, password, **extra_fields)

    def get_verified_users(self):
        """
        Email tasdiqlangan foydalanuvchilarni olish.
        """
        return self.filter(is_verified=True)

    def get_staff_users(self):
        """
        Staff (admin) huquqlariga ega foydalanuvchilarni olish.
        """
        return self.filter(is_staff=True)
