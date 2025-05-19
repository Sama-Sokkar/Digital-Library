from flask import get_flashed_messages

def flash_alerts(color):
    messages = get_flashed_messages()
    alert_script = ""

    if messages:
        for msg in messages:
            alert_script += f"""
            <script>
                document.addEventListener("DOMContentLoaded", function() {{
                    showAlert("{msg}" ,"{color}");
                }});
            </script>
            """
    return alert_script