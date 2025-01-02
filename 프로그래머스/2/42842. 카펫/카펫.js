function solution(brown, yellow) {
    for (var y = 3; y <= (brown + yellow)/y; y++){
        x = ((brown + yellow)/y);
        if((x-2)*(y-2) === yellow) {
            break;
        }
    }
    return [x,y];
}



















