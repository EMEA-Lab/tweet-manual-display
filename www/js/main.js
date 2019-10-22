function init() {    
    
    let addButton = document.querySelector('#add-button');
    
    addButton.addEventListener("click", function () {  
        
        let handleInput = document.querySelector('#tweet-input').value;        
        
        addTweet(handleInput);
        
    });
    
    function addTweet(tweetID) {
        
        let data = {}
        
        fetch('/add-tweet', {
                method: 'POST',
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