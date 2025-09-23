function solution(plans) {
    const queue = plans.map((plan) => {
        const [name, time, spend] = plan;
        const [hour, minute] = time.split(':');
        const convertTime = Number(hour)*60 + Number(minute);
        
        return {name, start: convertTime, spend:Number(spend)};
    })
    queue.sort((a,b) => a.start - b.start);
    
    const stack = [];
    const result = [];
    
    for(let i = 0; i < queue.length; i++) {
        const curr = queue[i];
        const nextStart = (i + 1 < queue.length) ? queue[i+1].start : Infinity;
        let available = nextStart - curr.start;
        
        let leftover = 0;
        
        if(available >= curr.spend){
            result.push(curr.name);
            leftover = available - curr.spend;
        
        
        while (leftover > 0 && stack.length){
            const top = stack.pop();
            if(leftover >= top.remain){
                leftover -= top.remain;
                result.push(top.name);
            } else {
                top.remain -= leftover;
                stack.push(top);
                leftover = 0;
            }
        }
    }  else {
      stack.push({ name: curr.name, remain: curr.spend - available });
    }
  }
    
    while(stack.length) {
        result.push(stack.pop().name)
    }
    
    return result
}