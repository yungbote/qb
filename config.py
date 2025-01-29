import os

# Disable logging (removes lag)
"""
os.environ["QT_LOGGING_RULES"] = "*=false"
"""
# Full GPU Acceleration
"""
c.qt.force_software_rendering = "none"
c.qt.args += [
    "--enable-gpu-rasterization",
    "--enable-zero-copy",
    "--ignore-gpu-blocklist",
    "--enable-native-gpu-memory-buffers",
    "--enable-accelerated-video-decode",
    "--enable-vulkan",
    "--enable-fast-unload",
    "--enable-oop-rasterization",
    "--use-gl=desktop",
    "--disable-gpu-driver-bug-workarounds",
]
"""

# Ultra-Low-Latency Keyboard Input
"""
c.qt.args += [
    "--disable-renderer-accessibility",
    "--disable-threaded-scrolling",
    "--disable-gesture-typing",
    "--disable-webrtc-hw-encoding",
    "--disable-webrtc-hw-decoding",
    "--disable-touch-adjustment",
    "--enable-low-latency-dxva",
    "--disable-vsync",
    "--enable-quic",
    "--disable-frame-rate-limit",
    "--disable-threaded-animation",
    "--enable-touch-events",
]
"""

# Force Faster Page Rendering
"""
c.qt.args += [
    "--disk-cache-size=536870912",  # 512MB Cache
    "--enable-simple-cache-backend",
    "--enable-best-effort-navigation",
    "--disable-blink-features=AutomationControlled",
    "--enable-new-base-cache",
    "--enable-async-image-decoding",
    "--enable-async-dns",
    "--enable-threaded-scrolling",
    "--enable-lazy-image-loading",
]
"""

# Remove Debugging & Security Warnings
"""
c.qt.args += [
    "--disable-logging",
    "--disable-dev-shm-usage",
    "--disable-logging-redirect",
    "--no-sandbox",
]
"""
c.content.tls.certificate_errors = "load-insecurely"

# Max FPS, No Laggy Scroll
c.scrolling.smooth = False
"""
c.qt.args += [
    "--enable-accelerated-2d-canvas",
    "--disable-scroll-bouncing",
    "--enable-threaded-compositing",
]
"""

# Optimized Background Tab Handling
c.tabs.background = True

# Disable Unneeded Features
c.content.notifications.enabled = False
c.content.media.audio_capture = False
c.content.media.video_capture = False
c.content.media.audio_video_capture = False
c.content.autoplay = False
c.content.cookies.accept = "all"
c.content.headers.accept_language = "en-US,en;q=0.9"
c.content.canvas_reading = True  # Fixes infinite redirects

# Load autoconfig
config.load_autoconfig(False)

# Cloudflare Fix
c.content.cookies.accept = "all"
c.content.headers.referer = "same-domain"

# General Performance Tweaks
c.messages.timeout = 1
c.statusbar.show = "never"
c.input.insert_mode.auto_load = False
c.auto_save.session = True
c.url.default_page = "about:blank"
#c.qt.force_platform = "xcb"

# Security Fixes
c.content.tls.certificate_errors = "load-insecurely"

# User Agent (Fixes site compatibility)
c.content.headers.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

# Start Page & Search Engine
c.url.start_pages = "https://google.com"
c.url.default_page = "https://google.com"
c.url.searchengines = {
    "DEFAULT": "https://google.com/?q={}",
    "gpt": "https://chatgpt.com/?q={}",
    "yt": "https://youtube.com/results?search_query={}",
    "w": "https://en.wikipedia.org/wiki/{}",
}

# UI Customization
c.zoom.default = "125%"
c.fonts.default_family = "JetBrainsMono Nerd Font"
c.fonts.default_size = "18pt"
c.fonts.web.family.standard = "JetBrainsMono Nerd Font"
c.fonts.web.family.fixed = "JetBrainsMono Nerd Font"
c.fonts.web.family.sans_serif = "JetBrainsMono Nerd Font"
c.fonts.web.family.serif = "JetBrainsMono Nerd Font"

# Colors & Theme
c.colors.completion.category.bg = "#1e2a38"
c.colors.completion.category.fg = "#ebcb8b"
c.colors.completion.item.selected.bg = "#3b4f63"
c.colors.completion.item.selected.fg = "#4c566a"
c.colors.statusbar.normal.bg = "#1e2a38"
c.colors.statusbar.normal.fg = "#ebcb8b"
c.colors.tabs.selected.even.bg = "#1e2a38"
c.colors.tabs.selected.odd.bg = "#33475b"

# Keybindings - Navigation
config.bind("h", "scroll left")
config.bind("l", "scroll right")
config.bind("j", "scroll down")
config.bind("k", "scroll up")

# Tab Management
config.bind("H", "tab-prev")
config.bind("L", "tab-next")
config.bind("x", "tab-close")
config.bind("u", "undo")
config.bind("t", "cmd-set-text -s :open -t")

# Link Navigation
config.bind("f", "hint")
config.bind("F", "hint all tab")
config.bind("v", "mode-enter caret")
config.bind("yv", "yank-selection")

# Quick Actions
config.bind("yy", "yank")
config.bind("p", "open -- {clipboard}")
config.bind("P", "open -t -- {clipboard}")

# Play Media Directly with MPV
config.bind("M", "hint links spawn mpv {hint-url}")

# JavaScript Settings
c.content.javascript.enabled = True
config.set("content.javascript.enabled", True, "*://trusted-sites/*")
config.set("content.javascript.enabled", True, "https://www.youtube.com")
config.set("content.javascript.enabled", True, "https://www.chatgpt.com")
config.set("content.javascript.enabled", True, "https://www.google.com")
config.set("content.javascript.enabled", True, "https://www.wikipedia.com")

# Hints Customization
c.hints.border = "1px solid  #D8B780"
c.hints.padding = {"top": 4, "bottom": 4, "left": 6, "right": 6}

# Downloads
c.downloads.location.directory = "~/Downloads"
c.downloads.remove_finished = 5000

# Dark Mode (Disabled by default)
c.colors.webpage.darkmode.enabled = False

# Zoom Controls
config.bind("+", "zoom-in")
config.bind("-", "zoom-out")
config.bind("=", "zoom")

# Search
config.bind("/", "cmd-set-text /")
config.bind("?", "cmd-set-text ?")
config.bind("n", "search-next")
config.bind("N", "search-prev")

# Downloads
config.bind("d", "cmd-set-text -s :download")
config.bind("D", "open qute://downloads")
config.bind("Ctrl-D", "download-clear")

# Bookmarks
config.bind("B", "cmd-set-text -s :bookmark-add")
config.bind("b", "cmd-set-text -s :open qute://bookmarks")
