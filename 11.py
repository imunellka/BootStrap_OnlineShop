from flask import Flask, url_for,request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                              <title>vitaminka</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <style>
  body {
    position: relative; 
  }

.jumbotron { 
  background-color: #f4511e; /* Orange */
  color: #fff;
}
  .navbar {
    margin-bottom: 0px;
  }
.form-group { 
  background-color: #f4511e; /* Orange */
  color: #fff;
}
  .affix ~ .container-fluid {
   position: relative;
   top: 30px;
  }

  </style>
                          </head>
                          <body data-spy="scroll" data-target=".navbar" data-offset="50" style="background-image:url('clouds.jpg');">>
                          <div class="container-fluid" style="background-color:#f4511e;color:#f4511e;height:240px;">
                       <div class="jumbotron text-center">
                       <h1>MAGAZIN</h1> 
                        <p>We specialize in clothes</p> 
                     </div>
                           </div>
                            <h1>Регистрация</h1>
                            <form method="post">
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                <button type="submit" class="btn btn-primary">submit</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
