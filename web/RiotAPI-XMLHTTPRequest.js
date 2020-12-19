require(['xmlhttprequest'], function (xmlhttprequest) {
    var XMLHttpRequest = require("xmlhttprequest");
});

var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
}
var client = new HttpClient();
client.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/munyoz1?api_key=(KEY DE RIOTAPI)', function(response) {
    console.log(response);
});
