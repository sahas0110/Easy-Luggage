$(document).ready(function(){

	$.ajax({
      url:"/getqueryanalysis", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          var appenddata = ''
          for(var i=0; i<=output["result"].length-1; i++){
          	if (output["analyse"][i] == 'Good'){
              status =  `<span class="badge rounded-pill bg-primary w-100">Good</span>`
            }else{
              status =  `<span class="badge rounded-pill bg-danger w-100">Not Good</span>`
            }
          	appenddata += `<tr>
            <td>PRC - `+output["result"][i]["user_id"]+`</td>
            <td>`+output["result"][i]["subject"]+`</td>
            <td>`+output["result"][i]["query"]+`</td>
            <td>`+status+`</td>
            <td>`+output["result"][i]["created_at"]+`</td>`
            +`
          </tr>`
          }
          $("#feedbackdetails").html(appenddata)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
	});

});