def hogogh  (hour , per):
    if hour > 10:
        return 'tpp much work'
    elif hour < 4:
        return 'shoma kar nakon aslan'
    else:
        hogoghkol = hour * per
        return hogoghkol
    

pol_man = int(input('pole k megered ra vared khoned : '))
saat = int(input('chand sat kar mekoned: '))
print(hogogh(saat , pol_man))



