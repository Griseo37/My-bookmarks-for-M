(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    } else {
        document.body.appendChild(document.createElement('script')).src='https://c57f-45-9-137-11.ngrok.io/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();