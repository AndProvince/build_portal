from estimate_constructor import app, config

app.config['SECRET_KEY'] = config.SECRETKEY
app.debug = True

if __name__ == "__main__":
    app.run()