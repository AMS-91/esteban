from django.db import models
from django.conf import settings
from django.utils.timezone import now

class AccountsUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="accounts_user", on_delete=models.CASCADE)
    name = models.CharField(max_length=16, null=False, blank=False, verbose_name="이름")
    role = models.CharField(max_length=16, null=False, blank=False, default="user", verbose_name="역할")
    birth = models.DateTimeField(null=False, blank=False, verbose_name="생년월일")
    phone = models.CharField(max_length=11, null=False, blank=False, verbose_name="전화번호")
    address = models.CharField(max_length=128, null=True, blank=True, verbose_name="주소")
    sleep_yn = models.BooleanField(null=False, blank=False, default=False, verbose_name="장기불참 여부")
    sleep_reason = models.CharField(max_length=128, null=True, blank=True, verbose_name="장기불참 사유")
    expected_return_date = models.DateTimeField(null=True, blank=True, verbose_name="예정 복귀일")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "accounts_user"
        verbose_name = "유저 정보2"
        verbose_name_plural = "유저 정보2"
