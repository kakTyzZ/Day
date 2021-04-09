import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from templates import Template

# environment variables
username = 'hungrypy@gmail.com'
password = 'LetsGetItStarted2020'

class Emailer():
    subject = "Hello World"
    to_emails = []
    has_html = False
    from_email='Hungry Py <hungrypy@gmail.com>'
    def __init__(self, subjec="", template_name=None, context{}, template_html=None, to_emails=None):
        if template_name ==None and template_html==None:
            raise Exception("You must set a template")
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        self.subject = subject
        if template_html != None:
            self.has_html = True

    def format_msg(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject

        if self.template_name != None:
            tmpl_str = Template(template_name=self.template_name, context=self.context)
            txt_part = MIMEText(tmpl_str.render(), 'plain')
            msg.attach(txt_part)

        if self.template_html != None:
            tmpl_str = Template(template_name=self.template_html, context=self.context)
            html_part = MIMEText(tmpl_str.render(), 'html')
            msg.attach(html_part)
        # txt_part = MIMEText(text, 'plain')
        # msg.attach(txt_part)
        # if html != None:
        #     html_part = MIMEText(html, 'html')
        #     msg.attach(html_part)
        msg_str = msg.as_string()
        return msg_str

    def send_mail(self):
        msg = self.format_msg()
        # login to my smtp server
        
        
        did_send = False
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.ehlo()
            server.starttls()
            server.login(username, password)
            try:
                server.sendmail(from_email, to_emails, msg_str)
                did_send = True
            except:
                did_send = False
        return did_send
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass