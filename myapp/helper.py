from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_forget_password_mail(email, otp_code):
    subject = f'Light Circle Varification Code: {otp_code}'
    
    html_content = f"""
    <html>
    <head>
     <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verification Code</title>
    <style>
        *{{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        body{{
            width: 100vw;
            margin: auto;
            max-width: 1050px;
            background-color: #f1f1f1;
            margin-top: 180px;
            text-align: center;
        }}
        img{{
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 5px solid #4f64ff;
            box-shadow: 0px 0px 10px #4f64ff;
            transition: transform 0.5s;
        }}
        .header{{
            background-color: #4f64ff;
            color: #fff;
            padding: 10px;
            text-align: center;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }}
         h2 {{
            font-size: 24px;
            margin-bottom: 20px;
        }}
        span {{
            padding: 10px 14px;
            border-radius: 5px;
            background-color: #4f64ff;
            color: #fff;
        }}
        span.otp {{
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .body{{
            font-size: 18px;
            line-height: 1.5;
            margin-top: 20px;
        }}
        footer{{
            background-color: #4f64ff;
            color: #fff;
            padding: 10px;
            text-align: center;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }}
    </style>
        
        
        
    </head>
    <body>
    <div class="header">
        <img src="https://scontent.fbbi3-1.fna.fbcdn.net/v/t39.30808-1/291652502_592919189192638_2330388367434845879_n.jpg?stp=dst-jpg_p200x200&_nc_cat=108&ccb=1-7&_nc_sid=f4b9fd&_nc_ohc=lBguXuz3oDsQ7kNvgEJEM87&_nc_ht=scontent.fbbi3-1.fna&oh=00_AYDQTvkblDQ3AYQb-BPuCWvd49Wt_isHKKFryLLTxsr7yA&oe=6695734D" alt="...">
        <h2>Light Circle</h2>
    </div>
    <div>
    <h2>Please enter this code to verify your account.</h2>
        <span class="otp">{otp_code}</span>
        <p class="body">This code is for account verification only. This code is not applicable for other porpose.</p>
    </div>
    <footer>
        <p>@ 2023 Light Circle. All rights reserved.</p>
    </footer>
    
</body>
    </html>
    """
    text_content = f'Please enter this code to verify your account {otp_code}'
    # message = f'Please enter this code to verify your account {otp_code}'
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return True

# def send_permission_mail(email):
#     subject = f'Light Circle message for join the team'
#     message = f'Please click the button to join the team {{http://127.0.0.1:8000/assign_permission/1/}}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, email_from, recipient_list)
#     return True
from django.core import signing

def generate_token(email):
    token = signing.dumps({'model_id': email})
    return token

def send_permission_mail(email):
    token = generate_token(email)
    link = f'http://127.0.0.1:8000/change_status/{token}/'
    subject = 'Change Status Request'
    html_content = f"""
        <html>
        <head>
            <style>
                /* Define your CSS styles here */
                body {{
                    width: 100vw;
                    margin: auto;
                    max-width: 1050px;
                    background-color: #f1f1f1;
                    margin-top: 180px;
                    font-family: Arial, sans-serif;
                }}
                img{{
                    width: 100px;
                    height: 100px;
                    border-radius: 50%;
                    border: 5px solid #4f64ff;
                    box-shadow: 0px 0px 10px #4f64ff;
                    transition: transform 0.5s;
                }}
                .header{{
                    background-color: #4f64ff;
                    color: #fff;
                    padding: 10px;
                    text-align: center;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    z-index: 1000;
                }}
                .middle-body{{
                    text-align: center;
                    width: 100%;
                    padding: 20px;
                    margin-bottom: 20px;
                }}
                p{{
                    font-size: 18px;
                    line-height: 1.5;
                }}
                
                button{{
                    background-color: #4f64ff;
                    color: #fff;
                    padding: 10px 20px;
                    border: none;
                    cursor: pointer;
                    transition: background-color 0.5s;
                    border-radius: 5px;
                    font-size: 20px;
                }}
                .button{{
                    color:#fff;
                }}
                footer{{
                    background-color: #4f64ff;
                    color: #fff;
                    padding: 10px;
                    text-align: center;
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    z-index: 1000;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                     <img src="https://scontent.fbbi3-1.fna.fbcdn.net/v/t39.30808-1/291652502_592919189192638_2330388367434845879_n.jpg?stp=dst-jpg_p200x200&_nc_cat=108&ccb=1-7&_nc_sid=f4b9fd&_nc_ohc=lBguXuz3oDsQ7kNvgEJEM87&_nc_ht=scontent.fbbi3-1.fna&oh=00_AYDQTvkblDQ3AYQb-BPuCWvd49Wt_isHKKFryLLTxsr7yA&oe=6695734D" alt="...">
                 <h2>Light Circle</h2>
                 </div>
            <div class="middle-body">
                <h3>Join your team on Light Circle</h3>
                <p>This is a Inventory management System by Light Circle.Join Out team on Light Circle </p>
                <p>user has invited you to join  team on Light Circle</p>
                <a class="button" href="{link}"><button>Join Team</button></a>
                <p>Control your stock with our simple, easy-to-use inventory management software. Start collaborating with your team in real-time across multiple devices and enhance your stock control productivity.</p>
                <hr>
            </div>
            <footer>
                <p>@ 2023 Light Circle. All rights reserved.</p>
            </footer>
            </div>
        </body>
        </html>
    """
    text_content = f'Please click the following link to change the status: {link}'

    # Send the email
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return True
    # message = f'Please click the following link to change the status: {link}'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail(subject, message, email_from, recipient_list)
    # return True