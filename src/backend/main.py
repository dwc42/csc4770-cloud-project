import webview
from backend.ticker import updateTicker

print("running")


webview.start(updateTicker, debug=True)
