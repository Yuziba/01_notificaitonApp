from plyer import notification

url_o = "iconum.ico"
notification.notify(title="Bildirim Başlığı",
                    message="Bildirim Açıklaması",
                    app_icon=url_o,
                    app_name="notifireBen",
                    timeout=10)
