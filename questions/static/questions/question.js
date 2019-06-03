function like(pk){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	  if (this.readyState == 4 && this.status == 200) {
		    var reply = JSON.parse(xhttp.responseText);
		    //this will give the number of likes
		    document.getElementById('answer-'+pk).innerHTML = reply["likes"];
	  }
	};
	xhttp.open("GET", "/like/"+pk, true);
	xhttp.send(); 
}