function init() {        

    function getTweet() {
        
        fetch('/get-latest-tweet', {
                method: 'GET'
            })
            .then(response => response.json())    
            .then(jsonData => updateTweetHTML(unescape(jsonData['html'])))
            .catch(err => {
                //error block
            });
                    
    }
    
    function updateTweetHTML(HTMLString) {
        
        console.log(HTMLString);
        
        let introWrapper = document.querySelector('#tweet-wrapper');    
        
        introWrapper.innerHTML = HTMLString;
        
        twttr.widgets.load(
          document.getElementById("tweet-wrapper")
        );        
    }
    
    getTweet();
}

init();