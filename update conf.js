    db.sco.find({organizations:4652312, ntype: "sco", tpl_type: "standard"}).forEach(sco => {
        const child = sco.children; 
        const temp = [];
        child.forEach(item => { 
            if (item.ntype == "exercise") { 
                temp2=item;
                temp2.options= {"can_review" : 1,"instant_key" : 1,"only_show_finish_button_when_reach_last_question" : 1};
                temp.push(temp2);
            } else {
                temp.push(item);
            }   
        });
        printjson(temp)
        // db.sco.updateOne( { 'iid': sco.iid }, { $set: { children: temp } } );
    });

db.session.updateMany({course_iid:{$in:[9382045,9382039,9382034,9382028,9382018,9382012,9382005,9358486,7501169]},start_date:{$gt:1684748617}},{$set:{teachers:data}});
db.session.find({course_iid:2175775,start_date:{$gt:1684748617}},{name:1});