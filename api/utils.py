from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings


def get_signature_html(name, subject, message):
    """
    Returns a fully styled HTML email for auto-reply.
    """
    return f"""<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#f4f4f4;padding:30px 0;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" border="0">

    <!-- Header -->
    <tr>
        <td align="center" style="background:#1b1b1b;padding:30px;">
            <table cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td style="background:#1b1b1b;padding:14px 20px;border:2px solid #ffa500;">
                        <span style="color:#ffa500;font-family:'Courier New',monospace;font-size:26px;font-weight:bold;letter-spacing:3px;">&lt;OH/&gt;</span>
                    </td>
                </tr>
            </table>
        </td>
    </tr>

    <!-- Content -->
    <tr>
        <td style="background:#2a2a2a;padding:36px 40px;">
            <p style="color:#fff;font-size:16px;margin:0 0 16px;">Hi {name},</p>
            <p style="color:#ccc;font-size:15px;margin:0 0 16px;line-height:24px;">Thank you for your message! I've received it and will get back to you as soon as possible.</p>
            <p style="color:#ccc;font-size:15px;margin:0 0 12px;">Here's a copy of your message:</p>

            <!-- Message copy -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:24px;">
                <tr>
                    <td width="3" style="background:#ffa500;">&nbsp;</td>
                    <td style="background:#1b1b1b;padding:12px 16px;">
                        <p style="color:#ffa500;font-size:13px;margin:0 0 8px;"><strong>Subject:</strong> {subject}</p>
                        <p style="color:#aaa;font-size:14px;margin:0;line-height:22px;">{message.replace(chr(10), '<br>')}</p>
                    </td>
                </tr>
            </table>

            <!-- Divider -->
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:20px;">
                <tr><td style="border-top:1px solid #3a3a3a;font-size:0;line-height:0;">&nbsp;</td></tr>
            </table>

            <!-- Signature -->
            <p style="color:#fff;font-size:15px;margin:0 0 4px;">Best regards,</p>
            <p style="color:#ffa500;font-size:16px;font-weight:bold;margin:0 0 2px;">Omar Haji</p>
            <p style="color:#888;font-size:13px;margin:0 0 20px;">Software Developer</p>

            <!-- Links -->
            <table cellpadding="0" cellspacing="0" border="0">
                <tr><td style="padding-bottom:8px;">
                    <a href="mailto:contact@omarhaji.com" style="color:#ffa500;text-decoration:none;font-size:13px;">
                        <img src="https://cdn-icons-png.flaticon.com/16/732/732200.png" width="14" height="14" alt="Email" border="0" style="vertical-align:middle;margin-right:6px;">contact@omarhaji.com
                    </a>
                </td></tr>
                <tr><td style="padding-bottom:8px;">
                    <a href="https://www.omarhaji.com" style="color:#ffa500;text-decoration:none;font-size:13px;">
                        <span style="background:#1b1b1b;color:#ffa500;font-family:'Courier New',monospace;font-size:9px;font-weight:bold;padding:2px 4px;border:1px solid #ffa500;vertical-align:middle;margin-right:6px;">&lt;OH/&gt;</span>www.omarhaji.com
                    </a>
                </td></tr>
                <tr><td style="padding-bottom:8px;">
                    <a href="https://www.linkedin.com/in/omar-haji-0243b128b" style="color:#ffa500;text-decoration:none;font-size:13px;">
                        <img src="https://cdn-icons-png.flaticon.com/16/174/174857.png" width="14" height="14" alt="LinkedIn" border="0" style="vertical-align:middle;margin-right:6px;">LinkedIn
                    </a>
                </td></tr>
                <tr><td>
                    <a href="https://github.com/OmarHaji0001" style="color:#ffa500;text-decoration:none;font-size:13px;">
                        <img src="https://cdn-icons-png.flaticon.com/16/733/733553.png" width="14" height="14" alt="GitHub" border="0" style="vertical-align:middle;margin-right:6px;">GitHub
                    </a>
                </td></tr>
            </table>
        </td>
    </tr>

    <!-- Footer -->
    <tr>
        <td align="center" style="background:#1b1b1b;padding:16px;">
            <p style="color:#666;font-size:12px;margin:0;">&copy; Omar Haji &nbsp;&middot;&nbsp;
                <a href="https://www.omarhaji.com" style="color:#ffa500;text-decoration:none;">omarhaji.com</a>
            </p>
        </td>
    </tr>

</table>
</td></tr>
</table>
</body>
</html>"""


def send_contact_emails(name, email, subject, message):
    """
    Sends contact email to Omar and auto-reply to sender.
    """
    # Email to Omar
    EmailMessage(
        subject=f"{subject} - From {name}",
        body=f"From: {name} <{email}>\nSubject: {subject}\n\n{message}\n\n---\nReply to: {email}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.CONTACT_EMAIL],
        reply_to=[email],
    ).send(fail_silently=False)

    # Auto-reply to sender
    auto_reply = EmailMultiAlternatives(
        subject="Thanks for reaching out — Omar Haji",
        body=f"Hi {name},\n\nThank you for your message! I'll get back to you soon.\n\nBest regards,\nOmar Haji",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
        bcc=[settings.CONTACT_EMAIL],
    )
    auto_reply.attach_alternative(get_signature_html(name, subject, message), "text/html")
    auto_reply.send(fail_silently=False)