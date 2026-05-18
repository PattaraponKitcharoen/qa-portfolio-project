import re
from playwright.sync_api import Page, expect

# ==========================================
# TC-LOG-001: ตรวจสอบการเข้าสู่ระบบสำเร็จ (Happy Path)
# ==========================================
def test_login_success(page: Page):
    # Pre-condition: ไปที่หน้าเว็บ
    page.goto("https://www.saucedemo.com/")

    # Test Steps: กรอกข้อมูลและกดปุ่ม
    # เราใช้ page.locator() เพื่อหาช่องกรอกข้อมูลจาก ID ของมันในหน้าเว็บ
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Expected Result: ตรวจสอบผลลัพธ์
    # 1. เช็คว่า URL เปลี่ยนไปที่หน้า inventory.html หรือไม่
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    # 2. เช็คว่ามีคำว่า Products ขึ้นมาบนหน้าจอจริงๆ
    expect(page.locator(".title")).to_contain_text("Products")


# ==========================================
# TC-LOG-002: ตรวจสอบการเข้าสู่ระบบล้มเหลว (Negative Test)
# ==========================================
def test_login_wrong_password(page: Page):
    # Pre-condition: ไปที่หน้าเว็บ
    page.goto("https://www.saucedemo.com/")

    # Test Steps: กรอกรหัสผ่านผิด
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password123")
    page.locator("#login-button").click()

    # Expected Result: ตรวจสอบผลลัพธ์
    # เช็คว่ามีกล่อง Error โผล่ขึ้นมา และมีข้อความแจ้งเตือนที่ถูกต้อง
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")

# ==========================================
# TC-LOG-003: ตรวจสอบการเข้าสู่ระบบล้มเหลว (ฺBlank Test)
# ==========================================
def test_login_blank_both(page: Page):
    # Pre-condition: ไปที่หน้าเว็บ
    page.goto("https://www.saucedemo.com/")

    # Test Steps: ไม่กรอกข้อมูล
    page.locator("#login-button").click()

    # Expected Result: ตรวจสอบผลลัพธ์
    # เช็คว่ามีกล่อง Error โผล่ขึ้นมา และมีข้อความแจ้งเตือนที่ถูกต้อง
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Epic sadface: Username is required")

# ==========================================
# TC-LOG-004: ตรวจสอบการเข้าสู่ระบบล้มเหลว (ฺUsername Blank Test)
# ==========================================
def test_login_blank_username(page: Page):
    # Pre-condition: ไปที่หน้าเว็บ
    page.goto("https://www.saucedemo.com/")

    # Test Steps: กรอกแค่รหัสผ่าน
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Expected Result: ตรวจสอบผลลัพธ์
    # เช็คว่ามีกล่อง Error โผล่ขึ้นมา และมีข้อความแจ้งเตือนที่ถูกต้อง
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Epic sadface: Username is required")

# ==========================================
# TC-LOG-005: ตรวจสอบการเข้าสู่ระบบล้มเหลว (ฺPassword Blank Test)
# ==========================================
def test_login_blank_password(page: Page):
    # Pre-condition: ไปที่หน้าเว็บ
    page.goto("https://www.saucedemo.com/")

    # Test Steps: กรอกแค่ Username
    page.locator("#user-name").fill("standard_user")
    page.locator("#login-button").click()

    # Expected Result: ตรวจสอบผลลัพธ์
    # เช็คว่ามีกล่อง Error โผล่ขึ้นมา และมีข้อความแจ้งเตือนที่ถูกต้อง
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Epic sadface: Password is required")