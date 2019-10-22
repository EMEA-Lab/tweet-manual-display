function init() {    
    
    let addButton = document.querySelector('#add-button');
    
    addButton.addEventListener("click", function () {  
        
        let tweetInput = document.querySelector('#tweet-input').value;        
        
        addTweet(tweetInput);
        
    });
    
    function addTweet(tweetURL) {
        
        tweetIDArr = tweetURL.split('/');
        tweetID = tweetIDArr[tweetIDArr.length - 1];
        
        let data = {            
            'tweetID': tweetID
        }    
        
        fetch('/add-tweet', {
                method: 'POST',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },                
                body: JSON.stringify(data)
            })
            .then(response => response.json())    
            .then(jsonData => console.log(jsonData))
            .catch(err => {
                //error block
            });
            
            
    }
}

init();

