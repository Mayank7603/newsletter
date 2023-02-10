const express=require("express");
const bodyParser=require("body-parser");
const request =require("request");
const https=require("https");
const app=express();

app.use(bodyParser.urlencoded({extended:true}));

app.get("/",function(req,res){                          //sending this html to the local host serer that we have initiated 
    res.sendFile(__dirname+"/signUp.html");
})

app.use(express.static("public"));      // this is done beacuse we are going to have css and images in our local public folder so to make them accessible to the host we are storeing them in a folder named as  public and then passing that folder to the local host s


app.post("/",function(req,res){         // getting back the response of the data from our signup page
    console.log("Gf\n");
    const fname=req.body.firstName;
    const lname=req.body.lastName;
    const email=req.body.emailAdd;



    const data={                // all below is done to send the data in required format to the mailchimp api
        members :[
            {
            email_address:email,
            status:"subscribed",
            merge_fields: {
                FNAME: fname,
                LNAME: lname
            }
        }
        ]
    };

    const jsonData= JSON.stringify(data);
    const url="https://us21.api.mailchimp.com/3.0/lists/c01fa70335";

    const options ={                // authetication 
        method:"POST",
        auth : "mayank:7b308b54be8d055cc47c31664fc76922-us21"
    }

    const request = https.request(url, options, function (response) {      
        if (response.statusCode == 200) {
            res.sendFile(__dirname + "/success.html");
        } else {
            res.sendFile(__dirname + "/failure.html");
        }
    })
    request.write(jsonData);
    request.end();
})


// rerouting the user from the failure page
app.post("/failure", function (req, res) {
    res.redirect("/");
})



app.listen(3000,function(){
    console.log("server is started at port 3000");
});

// 7b308b54be8d055cc47c31664fc76922-us21
// c01fa70335