require(['foo'], function (foo) {
  request({url: 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/munyoz1?api_key=(KEY DE RIOTAPI)', json: true}, function (error, response, body) {
  console.error('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the HTML for the Google homepage.
  for (var key in body){
    console.log(key, body[key])
  }
      
});
});



