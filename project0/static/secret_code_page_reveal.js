// This Javascript is to check the secret code

function check_code_given() {
	event.preventDefault();
	var code = 0;
	if ($("#secret_code").val()) {
		code = $("#secret_code").val();
		
		if (code == 26257121986797368) {
			document.getElementById("secret_completed").innerHTML = "YOU ARE NOW A <a class='game_completed' href='/secret_page'>PANDAWAND</a>"
		} else {
			alert("CODE:"+code+" WRONG CODE... Try Again");
		}
	}
}