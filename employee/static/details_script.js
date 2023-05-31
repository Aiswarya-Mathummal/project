$(document).ready(function(){
    $("#regbtn").click(function(){
        $.ajax({
            url:'details',
            type:'get',
            datatype:'json',
            success:function(data){
                var obj= JSON.parse(data);
                $("#tb1").append("<tr><th>Firstname</th><th>Lastname</th><th>Age</th><th>Address</th><th>Phone Number</th><th>Email</th><th>Profile Photo</th></tr>");
                for($i=0;$i<=obj.length;$i++){
                    // $("#select").append("<option>"+obj[$i].fields.name+"</option>");
                    $("#tb1").append("<tr>");
                    $("#tb1").append("<td>"+obj[$i].fields.firstname+"</td>");
                    $("#tb1").append("<td>"+obj[$i].fields.lastname+"</td>");
                    $("#tb1").append("<td>"+obj[$i].fields.age+"</td>");
                    $("#tb1").append("<td>"+obj[$i].fields.address+"</td>");
                    $("#tb1").append("<td>"+obj[$i].fields.phone+"</td>");
                    $("#tb1").append("<td>"+obj[$i].fields.email+"</td>");
                    $("#tb1").append("<td>"+obj[$i].fields.photo+"</td>");
                    $("#tb1").append("</tr>");
                }
            },error:function(d1){
                console.log(d1)
            }

        });
    });
});