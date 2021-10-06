# RunDontCrawl
A simple battler. Digital/quick prototype for a card game idea.

Core Objectives of the game:
  1) Fun - Number one priority is it needs to be interesting and fun to play.
  2) Simple - My goal is for this to be available to be used in a quick RPG setting where rulebooks may have too many features, etc.
  3) Workable in a physical card system (ie. large enough number of cards to be interesting, but small enough to be affordable by most people)

Core Components:
  1) Scaled attack/defend options (ie. a simple attack vs. pushing hard for more results, etc.)
  2) Multiple "classes" and optimization features
  3) Deck-building capabilites (such as for leveling up)
  4) Digital interface is similar enough to actual card-gameplay.

Features to be added:
  1) More classes, more cards.
  2) Deck-building options
  3) Random choices for moves (see below).



Basic Card Game Components:
1) Player and enemy have a certain amount of Stamina that they can use each turn. This is influenced by their class stats (classes with more STR will generally have more HP, etc.) similar to most classic RPG's.
2) Characters have access to four types of moves - Press, Attack, Defend, and Evade. Press and Evade are similar in effect to Attack and Defend, but represent a "harder" move - For example, a "Press Forward" move such as Smash Defenses represents extra effort than a simple slash with an ax. This means Press and Evade require more Stamina and have higher Roll Conditions to be met (higher chance to fail), but have better results if successful (more damage dealt/blocked).
3) When a character selects a type of move, they will randomly draw cards from that deck of moves, select one, and execute that action. (For example, they may have 10 of each type of attack in front of them as their deck. When they choose to Press, they draw the first two cards of the Press deck, select one of the cards, and roll the die to use that attack. Both attacks will be discarded, and when the character uses all of the attacks in that deck, they will shuffle them back together and create a new draw pile).
4) Players have an AGI stat that affects their Hit Conditions (makes it easier to hit/block, etc.) and a STR stat that affects their HP and Damage Dealing amounts. (More stats may be added later, but in order to keep it simple, these are the only two currently).
5) If player does not have enough Stamina to continue with the action they want, they can make a "Basic" action. These take 0SP (or 1SP for Press and Evade actions) and have low results, but allow them to do something each turn.
6) SP refills slowly each turn.
