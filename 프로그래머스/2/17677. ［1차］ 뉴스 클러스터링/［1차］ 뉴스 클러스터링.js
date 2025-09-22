function solution(str1, str2) {
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    
    let str1_arr = [];
    let intersection = 0;
    let union = 0;
    
    const regex = /^[a-z]{2}$/;
    
    for(let i = 0; i < str1.length - 1; i++){
        const pair = str1.slice(i, i+2);
        if(regex.test(pair)){
            str1_arr.push(pair);
        }
    }
    
    union += str1_arr.length;
    
    for(let i = 0; i < str2.length - 1; i++){
        const pair = str2.slice(i, i+2);
        if(regex.test(pair)) {
            if(str1_arr.includes(pair)) {
                intersection++;
                str1_arr.splice(str1_arr.indexOf(pair), 1);
            } else{
                union++
            }
        }
    }
    return union === 0 ? 65536 : Math.floor((intersection/union)*65536);
}