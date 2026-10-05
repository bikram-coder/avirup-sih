import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('http://localhost:8501', timeout=30000)
    page.wait_for_timeout(5000)
    
    tabs = page.locator('[role="tab"]').all()
    print(f"role=tab count: {len(tabs)}")
    for i, t in enumerate(tabs):
        print(f"Tab {i+1}: {t.inner_text().strip()}")
        
    buttons = page.locator('button').all()
    print(f"\nAll buttons count: {len(buttons)}")
    for i, b in enumerate(buttons[:10]):
        print(f"Button {i+1}: {b.inner_text().strip()}")
        
    browser.close()
