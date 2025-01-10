function solution(bandage, health, attacks) {
    const maxHP = health;
    const [t, x, y] = bandage;
    
    let lastAttackTime = 0;
    
    for (const [attacktime, damage] of attacks) {
        // 공격 받는 동안 회복
        const timeDiff = attacktime - lastAttackTime -1;
        const heal = timeDiff * x + Math.floor(timeDiff/t) * y;
        health = Math.min(health + heal, maxHP);
        // 공격 적용
        health -= damage;
        
        if(health <= 0) {
            return -1;
        }
        
        lastAttackTime = attacktime
    }
    return health;
}