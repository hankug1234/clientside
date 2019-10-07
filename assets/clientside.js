if (!window.dash_clientside) { window.dash_clientside = {}; }
window.dash_clientside.clientside = {
    update: function (value) {

        if(value==0)
          return no_update;

     function arrayBufferToBase64(buffer) {
    let binary = '';
    let bytes = new Uint8Array(buffer);
    let len = bytes.byteLength;
    for (let i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    return window.btoa(binary);
}

var httpRequest = new XMLHttpRequest();
     var response;
     if(window.XMLHttpRequest)
     {
       httpRequest = new XMLHttpRequest();
     }
     else if(window.ActiveXObject)
     {
      httpRequest = new ActiveXObject('Microsoft.XMLHTTP');
     }
     var response;


     httpRequest.open('GET','http://127.0.0.1:5007/data',false);
     httpRequest.send(null);

     response = JSON.parse(httpRequest.responseText);

     var encoded_image = null;

    if(response['data'] == '404')
       return no_update;
    else
        encoded_image = arrayBufferToBase64(response['data']['image']);


    return 'data:image/jpg;base64,' + window.atob(encoded_image);

    }
}