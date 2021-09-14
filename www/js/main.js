function init() {        
    
    var currentTweetURL = '';
    var currentTweetDisplay = 0;
    let tweetWrapper1 = document.getElementById('tweet-wrapper-1');
    let tweetWrapper2 = document.getElementById('tweet-wrapper-2');    
    
    function getTweet() {
        
        fetch('/get-latest-tweet', {
                method: 'GET'
            })
            .then(response => response.json())    
            .then(jsonData => checkTweetAndUpdate(jsonData))
            .catch(err => {
                //error block
            });
                    
    }
    
    function checkTweetAndUpdate(tweetData) {
        
        if(tweetData['url'] !== currentTweetURL) {
            
            currentTweetURL = tweetData['url'];
            updateTweetHTML(unescape(tweetData['html']));
                    
        } else {
            
            console.log('Same Tweet');
            
        }
        
        
    }
    
    function updateTweetHTML(HTMLString) {        
        
        var tweetToDisplay,
            tweetToFadeOut;        
        
        console.log(tweetWrapper1);   
                
        if(!currentTweetDisplay || currentTweetDisplay == 2) {
            tweetToDisplay = tweetWrapper1;
            tweetToFadeOut = tweetWrapper2;
            currentTweetDisplay = 1;               
        } else {
            tweetToDisplay = tweetWrapper2
            tweetToFadeOut = tweetWrapper1;            
            currentTweetDisplay = 2;            
        }
                        
        tweetToDisplay.innerHTML = HTMLString;
          
        
        twttr.widgets.load(
          tweetToDisplay
        );        
        
        twttr.events.bind(
          'loaded',
          function (event) {
            event.widgets.forEach(function (widget) {
              console.log("Created widget", widget.id);
            });
            
            
            tweetToDisplay.style['opacity'] = '1';
            tweetToFadeOut.style['opacity'] = '0';       
          }
        );        
    }
    
    setInterval(getTweet, 5000);
}

init();