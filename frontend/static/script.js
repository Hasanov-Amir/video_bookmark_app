const userAction = async () => {
    const response = await fetch('http://127.0.0.1:8080/0/content');
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson);
}

userAction()