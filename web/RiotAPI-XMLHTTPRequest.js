require(['xmlhttprequest'], function (foo) {
    var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
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
client.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/munyoz1?api_key=RGAPI-c99e8baa-f826-4750-bc01-7a1b34c169c6', function(response) {
    console.log(response);
});