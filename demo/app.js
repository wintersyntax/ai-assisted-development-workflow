const stages=[...document.querySelectorAll(".stage")];
const panels=[...document.querySelectorAll(".panel")];

function showStage(index){
  stages.forEach((button,i)=>button.classList.toggle("active",i===index));
  panels.forEach((panel,i)=>panel.classList.toggle("active",i===index));
}

stages.forEach((button,index)=>{
  button.addEventListener("click",()=>showStage(index));
});

document.querySelectorAll("[data-goto-stage]").forEach((button)=>{
  button.addEventListener("click",()=>{
    const index=Number(button.dataset.gotoStage);
    if(Number.isInteger(index) && index>=0 && index<stages.length){
      showStage(index);
    }
  });
});

document.addEventListener("keydown",(event)=>{
  const current=stages.findIndex(button=>button.classList.contains("active"));
  if(event.key==="ArrowRight") showStage(Math.min(stages.length-1,current+1));
  if(event.key==="ArrowLeft") showStage(Math.max(0,current-1));
});
