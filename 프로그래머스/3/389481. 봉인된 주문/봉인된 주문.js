function solution(n, bans) {
    const banned = new Set(bans);
    
    function getTotalCountUpTo(length) {
        let count = 0n;
        for (let i = 1; i <= length; i++) {
            count += 26n ** BigInt(i);
        }
        return count;
    }
    
    function findString(position) {
        let length = 1;
        let totalBeforeLength = 0n;
        let totalAtLength = 26n ** BigInt(length);
        
        while (position > totalBeforeLength + totalAtLength) {
            totalBeforeLength += totalAtLength;
            length++;
            totalAtLength = 26n ** BigInt(length);
        }
        
        let posInLength = position - totalBeforeLength - 1n;
        
        let result = '';
        for (let i = 0; i < length; i++) {
            const charCode = Number(posInLength / (26n ** BigInt(length - i - 1)) % 26n);
            result += String.fromCharCode(charCode + 97);
        }
        
        return result;
    }

    function getPosition(str) {
        const length = str.length;
        
        let position = getTotalCountUpTo(length - 1);
        
        let posInLength = 0n;
        for (let i = 0; i < length; i++) {
            posInLength = posInLength * 26n + BigInt(str.charCodeAt(i) - 97);
        }
        
        return position + posInLength + 1n;
    }
    
    const sortedBans = [...bans].map(ban => ({
        str: ban,
        pos: getPosition(ban)
    })).sort((a, b) => (a.pos < b.pos ? -1 : 1));
    
    let n_big = BigInt(n);
    let skips = 0n;
    
    for (const ban of sortedBans) {
        if (ban.pos - skips <= n_big) {
            skips++;
        } else {
            break;
        }
    }

    return findString(n_big + skips);
}