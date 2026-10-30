p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
if "android.speech.RecognitionService" not in s:
    add = """    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <queries>
        <intent><action android:name="android.speech.RecognitionService" /></intent>
        <intent><action android:name="android.intent.action.VIEW" /><data android:scheme="https" /></intent>
        <intent><action android:name="android.intent.action.DIAL" /></intent>
    </queries>
"""
    s = s.replace("</manifest>", add + "</manifest>")
    open(p, "w", encoding="utf-8").write(s)
print("manifest patched")
