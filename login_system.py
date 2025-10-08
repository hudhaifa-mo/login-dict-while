# -*- coding: utf-8 -*-
# نظام تسجيل دخول باستخدام Dictionary + while

from getpass import getpass

# بيانات المستخدم
user = {
    "username": "hudhaifa",
    "pass": "12345678",
    "name": "Hudhaifa Mohammed Noaman",
    "age": 20,
    "mail": "huthaifamo4@gmail.com",
}

attempts = 3
account_locked = False

while attempts > 0 and not account_locked:
    u = input("أدخل اسم المستخدم: ").strip()
    p = getpass("أدخل كلمة المرور: ")

    if u == user.get("username") and p == user.get("pass"):
        print("\n✅ تسجيل دخول ناجح!")
        print(f"مرحباً يا {user.get('name', 'مستخدم')} 👋")
        print("معلومات حسابك:")
        for k, v in user.items():
            if k == "pass":
                continue
            print(f"- {k}: {v}")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"❌ بيانات غير صحيحة. تبقى لديك {attempts} محاولة.")
        else:
            user.clear()
            account_locked = True
            print("\n⛔ تم إدخال بيانات خاطئة 3 مرات.")
            print("🔒 تم إقفال الحساب وحذف جميع البيانات من القاموس.")
