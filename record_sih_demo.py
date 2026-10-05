import os
import sys
import time
from playwright.sync_api import sync_playwright

# Exact audio durations (in seconds):
DURATIONS = [
    54.62,  # Audio 1: Crisis Demo & Pitch
    50.26,  # Audio 2: Forward Curve & Provenance
    48.09,  # Audio 3: Port Digital Twins
    52.92,  # Audio 4: Contract Optimizer & Fleet Positioning
    49.06,  # Audio 5: Tender Brief & Audit Ledger
    44.70   # Audio 6: Green Steel ESG & Final Pitch
]

OUTPUT_DIR = os.path.abspath("./recordings")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def inject_cursor_highlighter(page):
    """Injects a visible glowing cursor so YouTube viewers can follow interactions clearly."""
    js = """
    (() => {
        if (window._cursorInjected) return;
        window._cursorInjected = true;
        const cursor = document.createElement('div');
        cursor.id = 'playwright-mouse-cursor';
        cursor.style.width = '22px';
        cursor.style.height = '22px';
        cursor.style.border = '2px solid #ffffff';
        cursor.style.borderRadius = '50%';
        cursor.style.position = 'fixed';
        cursor.style.pointerEvents = 'none';
        cursor.style.zIndex = '999999';
        cursor.style.backgroundColor = 'rgba(239, 68, 68, 0.7)';
        cursor.style.boxShadow = '0 0 12px rgba(239, 68, 68, 0.9)';
        cursor.style.transform = 'translate(-50%, -50%)';
        cursor.style.transition = 'width 0.15s, height 0.15s, background-color 0.15s';
        document.body.appendChild(cursor);

        window.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });
        window.addEventListener('mousedown', () => {
            cursor.style.width = '14px';
            cursor.style.height = '14px';
            cursor.style.backgroundColor = 'rgba(34, 197, 94, 0.9)';
        });
        window.addEventListener('mouseup', () => {
            cursor.style.width = '22px';
            cursor.style.height = '22px';
            cursor.style.backgroundColor = 'rgba(239, 68, 68, 0.7)';
        });
    })();
    """
    page.evaluate(js)

def smooth_scroll(page, delta_y, steps=25, delay=0.03):
    step = delta_y / steps
    for _ in range(steps):
        page.evaluate(f"window.scrollBy({{top: {step}, behavior: 'auto'}});")
        time.sleep(delay)

def smooth_scroll_to(page, target_y, steps=25, delay=0.03):
    current = page.evaluate("window.scrollY")
    delta = target_y - current
    smooth_scroll(page, delta, steps, delay)

def smooth_mouse_move(page, target_x, target_y, steps=20):
    page.mouse.move(target_x, target_y, steps=steps)
    time.sleep(0.1)

def run_recording():
    print("======================================================")
    print("Starting Playwright Automated Recording for SIH")
    print(f"Target URL: http://localhost:8501")
    print(f"Total Sections: {len(DURATIONS)}")
    print(f"Total Duration Planned: {sum(DURATIONS):.2f}s (~5 mins)")
    print("======================================================")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-infobars"
            ]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir=OUTPUT_DIR,
            record_video_size={"width": 1920, "height": 1080}
        )
        page = context.new_page()

        print("Loading Dashboard...")
        page.goto("http://localhost:8501", timeout=60000)
        page.wait_for_timeout(4000)
        inject_cursor_highlighter(page)

        # Locate tabs
        tabs = page.locator('[role="tab"]').all()
        print(f"Detected {len(tabs)} tabs.")

        # ====================================================
        # SECTION 1: Introduction & Live Crisis Demo (~54.6s)
        # ====================================================
        sec1_start = time.time()
        print(">>> Recording Section 1: Intro & Crisis Demo")
        inject_cursor_highlighter(page)
        
        # Click Tab 1 if needed
        if len(tabs) > 0:
            tabs[0].click()
            time.sleep(1)

        # Smooth move to masthead
        smooth_mouse_move(page, 500, 120)
        time.sleep(3)

        # Scroll to crisis banner
        smooth_scroll(page, 200, steps=20)
        time.sleep(2)

        # Click Crisis Simulation Button
        crisis_btn = page.locator('button:has-text("Trigger \'Day in the Life\' Crisis Simulation")')
        if crisis_btn.count() > 0:
            box = crisis_btn.bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.5)
                crisis_btn.click()
                print("  Triggered Crisis Simulation button!")
        
        time.sleep(4)
        inject_cursor_highlighter(page)

        # Scroll down through KPI cards
        smooth_scroll(page, 300, steps=25)
        time.sleep(4)

        # Move mouse across KPI cards to highlight them
        smooth_mouse_move(page, 350, 450)
        time.sleep(2)
        smooth_mouse_move(page, 750, 450)
        time.sleep(2)
        smooth_mouse_move(page, 1150, 450)
        time.sleep(2)
        smooth_mouse_move(page, 1550, 450)
        time.sleep(2)

        # Scroll down to shock events and autonomous SOPs
        smooth_scroll(page, 450, steps=30)
        time.sleep(5)
        smooth_scroll(page, 350, steps=25)
        time.sleep(4)

        # Scroll back up to tabs for next section
        smooth_scroll_to(page, 150, steps=30)
        sec1_elapsed = time.time() - sec1_start
        remaining1 = DURATIONS[0] - sec1_elapsed
        if remaining1 > 0:
            time.sleep(remaining1)
        print(f"  Section 1 completed in {time.time() - sec1_start:.2f}s (Target: {DURATIONS[0]}s)")

        # ====================================================
        # SECTION 2: Forward Curve & ML Price Forecasting (~50.3s)
        # ====================================================
        sec2_start = time.time()
        print(">>> Recording Section 2: Forward Curve & Provenance")
        tabs = page.locator('[role="tab"]').all()
        if len(tabs) > 1:
            box = tabs[1].bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.3)
            tabs[1].click()
        time.sleep(3)
        inject_cursor_highlighter(page)

        # Inspect the forward curve
        smooth_scroll(page, 250, steps=20)
        time.sleep(4)

        # Move mouse across forward curve chart
        smooth_mouse_move(page, 700, 500)
        time.sleep(2)
        smooth_mouse_move(page, 1100, 480)
        time.sleep(2)

        # Scroll to historical metrics & confidence interval
        smooth_scroll(page, 400, steps=25)
        time.sleep(5)
        smooth_scroll(page, 350, steps=25)
        time.sleep(5)

        # Scroll to provenance disclosure
        smooth_scroll(page, 300, steps=20)
        time.sleep(4)

        smooth_scroll_to(page, 150, steps=30)
        sec2_elapsed = time.time() - sec2_start
        remaining2 = DURATIONS[1] - sec2_elapsed
        if remaining2 > 0:
            time.sleep(remaining2)
        print(f"  Section 2 completed in {time.time() - sec2_start:.2f}s (Target: {DURATIONS[1]}s)")

        # ====================================================
        # SECTION 3: Port Digital Twins (~48.1s)
        # ====================================================
        sec3_start = time.time()
        print(">>> Recording Section 3: Port Digital Twins")
        tabs = page.locator('[role="tab"]').all()
        if len(tabs) > 2:
            box = tabs[2].bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.3)
            tabs[2].click()
        time.sleep(3)
        inject_cursor_highlighter(page)

        # Scroll down through port twins
        smooth_scroll(page, 300, steps=25)
        time.sleep(4)

        # Highlight Paradip, Haldia, Visakhapatnam cards
        smooth_mouse_move(page, 400, 400)
        time.sleep(2.5)
        smooth_mouse_move(page, 950, 400)
        time.sleep(2.5)
        smooth_mouse_move(page, 1450, 400)
        time.sleep(2.5)

        # Scroll to congestion bottleneck heatmap
        smooth_scroll(page, 400, steps=25)
        time.sleep(5)
        smooth_scroll(page, 350, steps=25)
        time.sleep(5)

        smooth_scroll_to(page, 150, steps=30)
        sec3_elapsed = time.time() - sec3_start
        remaining3 = DURATIONS[2] - sec3_elapsed
        if remaining3 > 0:
            time.sleep(remaining3)
        print(f"  Section 3 completed in {time.time() - sec3_start:.2f}s (Target: {DURATIONS[2]}s)")

        # ====================================================
        # SECTION 4: Contract Optimizer & Fleet Positioning (~52.9s)
        # ====================================================
        sec4_start = time.time()
        print(">>> Recording Section 4: Contract Optimizer & Fleet Positioning")
        tabs = page.locator('[role="tab"]').all()
        if len(tabs) > 3:
            box = tabs[3].bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.3)
            tabs[3].click()
        time.sleep(3)
        inject_cursor_highlighter(page)

        # Scroll through contract optimizer
        smooth_scroll(page, 300, steps=25)
        time.sleep(4)
        smooth_mouse_move(page, 800, 450)
        time.sleep(3)
        smooth_scroll(page, 400, steps=25)
        time.sleep(5)

        # Switch to Tab 5: Fleet & Ballast Positioning halfway through
        smooth_scroll_to(page, 150, steps=25)
        time.sleep(1)
        tabs = page.locator('[role="tab"]').all()
        if len(tabs) > 4:
            box = tabs[4].bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.3)
            tabs[4].click()
        time.sleep(3)
        inject_cursor_highlighter(page)

        # Show Fleet Positioning Radar
        smooth_scroll(page, 300, steps=25)
        time.sleep(4)
        smooth_mouse_move(page, 600, 500)
        time.sleep(2.5)
        smooth_scroll(page, 350, steps=20)
        time.sleep(4)

        smooth_scroll_to(page, 150, steps=30)
        sec4_elapsed = time.time() - sec4_start
        remaining4 = DURATIONS[3] - sec4_elapsed
        if remaining4 > 0:
            time.sleep(remaining4)
        print(f"  Section 4 completed in {time.time() - sec4_start:.2f}s (Target: {DURATIONS[3]}s)")

        # ====================================================
        # SECTION 5: Tender Brief & Tamper-Evident Audit (~49.1s)
        # ====================================================
        sec5_start = time.time()
        print(">>> Recording Section 5: Tender Brief & Audit Ledger")
        tabs = page.locator('[role="tab"]').all()
        if len(tabs) > 5:
            box = tabs[5].bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.3)
            tabs[5].click()
        time.sleep(3)
        inject_cursor_highlighter(page)

        # Showcase automated tender brief
        smooth_scroll(page, 300, steps=25)
        time.sleep(4)
        smooth_scroll(page, 350, steps=25)
        time.sleep(4)

        # Switch to Tab 7: Tamper-Evident Audit Ledger
        smooth_scroll_to(page, 150, steps=25)
        time.sleep(1)
        tabs = page.locator('[role="tab"]').all()
        if len(tabs) > 6:
            box = tabs[6].bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.3)
            tabs[6].click()
        time.sleep(3)
        inject_cursor_highlighter(page)

        # Highlight SHA-256 Audit Trail & Hash-Chained ledger
        smooth_scroll(page, 300, steps=25)
        time.sleep(4)
        smooth_mouse_move(page, 700, 480)
        time.sleep(3)
        smooth_scroll(page, 400, steps=25)
        time.sleep(4)

        smooth_scroll_to(page, 150, steps=30)
        sec5_elapsed = time.time() - sec5_start
        remaining5 = DURATIONS[4] - sec5_elapsed
        if remaining5 > 0:
            time.sleep(remaining5)
        print(f"  Section 5 completed in {time.time() - sec5_start:.2f}s (Target: {DURATIONS[4]}s)")

        # ====================================================
        # SECTION 6: Green Steel ESG & Pitch Conclusion (~44.7s)
        # ====================================================
        sec6_start = time.time()
        print(">>> Recording Section 6: Green Steel ESG & Conclusion")
        tabs = page.locator('[role="tab"]').all()
        if len(tabs) > 7:
            box = tabs[7].bounding_box()
            if box:
                smooth_mouse_move(page, box["x"] + box["width"]/2, box["y"] + box["height"]/2)
                time.sleep(0.3)
            tabs[7].click()
        time.sleep(3)
        inject_cursor_highlighter(page)

        # Showcase Scope 3 carbon footprint & green corridor
        smooth_scroll(page, 300, steps=25)
        time.sleep(4)
        smooth_mouse_move(page, 600, 450)
        time.sleep(3)
        smooth_scroll(page, 350, steps=25)
        time.sleep(5)

        # Final return to top overview & masthead for concluding pitch
        smooth_scroll_to(page, 0, steps=30)
        time.sleep(3)
        smooth_mouse_move(page, 960, 150)
        time.sleep(4)

        sec6_elapsed = time.time() - sec6_start
        remaining6 = DURATIONS[5] - sec6_elapsed
        if remaining6 > 0:
            time.sleep(remaining6)
        print(f"  Section 6 completed in {time.time() - sec6_start:.2f}s (Target: {DURATIONS[5]}s)")

        print("Recording finished! Finalizing video context...")
        context.close()
        video_path = page.video.path()
        print(f"Video saved to: {video_path}")
        browser.close()

    return video_path

if __name__ == "__main__":
    run_recording()
