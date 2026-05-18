import re
from playwright.sync_api import Page, expect

# ==========================================
# TC-WKF-001: ตรวจสอบกระบวนการสั่งซื้อสินค้าตั้งแต่ต้นจนจบ (E2E Happy Path)
# ==========================================
def test_checkout_happy_path(page: Page):
    # --- Pre-conditions: ล็อกอินและไปที่หน้าสินค้า ---
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # --- Test Steps ---
    # 1. กดเพิ่มสินค้า 2 ชิ้น
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
    
    # 2. คลิกที่ไอคอนตะกร้าสินค้า
    page.locator("[data-test='shopping-cart-link']").click()
    
    # 3. คลิกปุ่ม Checkout
    page.locator("[data-test='checkout']").click()
    
    # 4. กรอกข้อมูลที่อยู่
    page.locator("[data-test='firstName']").fill("John")
    page.locator("[data-test='lastName']").fill("Doe")
    page.locator("[data-test='postalCode']").fill("12345")
    
    # 5. คลิกปุ่ม Continue
    page.locator("[data-test='continue']").click()
    
    # 6. ตรวจสอบหน้ารวมยอด แล้วคลิกปุ่ม Finish
    page.locator("[data-test='finish']").click()
    
    # --- Expected Result ---
    # ตรวจสอบข้อความสั่งซื้อสำเร็จ
    expect(page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")
    
    # 7. คลิกปุ่ม Back Home
    page.locator("[data-test='back-to-products']").click()
    
    # ตรวจสอบว่ากลับมาหน้าสินค้าหลัก
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))


# ==========================================
# TC-WKF-002: ตรวจสอบการเว้นว่างช่องกรอกที่อยู่ (Negative Test)
# ==========================================
def test_checkout_missing_last_name(page: Page):
    # --- Pre-conditions: ล็อกอินและไปที่หน้าสินค้า ---
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # --- Test Steps ---
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='checkout']").click()
    
    # กรอกข้อมูลไม่ครบ (จงใจเว้นว่าง Last Name)
    page.locator("[data-test='firstName']").fill("John")
    page.locator("[data-test='postalCode']").fill("12345")
    
    # คลิกปุ่ม Continue
    page.locator("[data-test='continue']").click()
    
    # --- Expected Result ---
    # ตรวจสอบว่ามี Error แจ้งเตือนเรื่อง Last Name
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Error: Last Name is required")