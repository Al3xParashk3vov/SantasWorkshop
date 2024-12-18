from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from SantasWorkshop.accounts.models import Profile


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

        # def save(self, commit=True):
        #     user = super().save(commit=False)
        #     elf_images = [f for f in default_storage.listdir('elf') if f.endswith('.jpg')]
        #     if elf_images:
        #         elf_image = random.choice(elf_images)
        #         elf_file = default_storage.open('elf/' + elf_image)
        #         elf_image_name = 'elf_' + get_random_string(10) + '.jpg'
        #         user.profile.elf_image.save(elf_image_name, ImageFile(elf_file), save=False)
        #     if commit:
        #         user.save()
        #     return user

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'image']
