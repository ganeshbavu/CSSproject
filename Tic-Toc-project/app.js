let boxes=document.querySelectorAll(".box");
let ResetButn=document.querySelector("#reset");

let turn0=true;
const winPattern=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,6,8],
    [0,4,8],
    [6,4,2],];
boxes.forEach((box)=>{
    box.addEventListener("click",()=>{
        console.log("box was clicked");
        if(turn0){
            box.innerText="0";
            turn0=false;
        }else{
            box.innerText="X";
            turn0=true;
        }
        box.display=true;
        checkWinner();
    });
});
const checkWinner=()=>{
    for(pattern of winPattern){
       let pos1val=boxes[pattern[0]].innerText;
       let pos2val=boxes[pattern[1]].innerText;
       let pos3val=boxes[pattern[2]].innerText;
       if (pos1val!=""&& pos2val!="" && pos3val!=""){
        if(pos1val==pos2val&&pos2val==pos3val){
            console.log("Winner");
        }
       }
    }
};