"""
Net Worth POV - Video 6: "POV: You Cleared $40,000 of Debt on a Normal Salary - Step by Step"
Cifras ilustrativas: deudas 12,000 tarjeta 24% (min 360) + 6,000 prestamo 11% (min 150) + 22,000 auto 7% (min 400) = 40,000, minimos 910/mes; Sam paga 1,200/mes (910 + 290 extra). Avalancha ~40 meses, interes ~7,700; bola de nieve ~41 meses, interes ~8,900; solo minimos ~67 meses, interes ~14,100.
Uso: python netWorthPOV_v6_scenes.py
"""
from nwpov_common import emit

S = []
def sc(kind, setting, visual, narr):
    S.append((kind, setting, visual, narr))

# ---- gancho ----
sc("MACRO", "DESK", "a plain blue credit card cut cleanly into two pieces on a dark wooden table, a small pair of scissors beside them, no letters and no digits.",
   "On a wooden table lie two halves of a credit card, and the scissors that did the work.")
sc("SIT", "KDAY", "he sits at the kitchen table at night with a white mug, a smartphone lying face down beside it, a calm slight smile, one lamp glowing.",
   "It is an ordinary Thursday night, and the last payment on your last loan just went through.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a pale card app with a small green check icon and no other marks, no readable text and no digits.",
   "There is no email with confetti. Just a quiet notification, and a balance that finally says zero.")
sc("CLOSE", "KDAY", "his face in close-up, eyes soft, a slow exhale, warm lamp light.",
   "You expected to cheer. Instead you feel something stranger, like setting down a very heavy bag.")
sc("WIDE", "KDAY", "a wide view of the kitchen, a refrigerator with a hand-drawn paper chart taped to it, three colored horizontal bars all erased, Sam small at the table.",
   "On the refrigerator hangs a paper chart with three colored bars. Tonight, all three are gone.")
sc("STAND", "KDAY", "he stands beside the refrigerator touching the paper chart with two fingers, a thoughtful smile.",
   "Three and a half years ago, those bars added up to forty thousand dollars. Your salary was perfectly normal.")
sc("SIT", "KDAY", "he sits at the table looking at the camera, a small ordinary shrug, no objects but the mug.",
   "No windfall. No inheritance. Just a plan you followed even when it was boring.")
sc("MACRO", "CLEAN", "a large flat icon of two left-pointing arrows in a rewind symbol, thick dark outline, centered on a plain cream wall, no text.",
   "So let us rewind to the month you finally looked at the whole pile.")

# ---- acto 2: el punto de partida ----
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a small stack of gray envelopes in front of him, one hand hovering over them, a single lamp glowing.",
   "At twenty-nine, you have a small stack of envelopes that you have been avoiding for months.")
sc("HAND", "KNIGHT", "a hand slowly tearing open a gray envelope, the edge of the paper curling, dark wooden table below.",
   "You open them one by one, because not knowing has started to feel worse than knowing.")
sc("MACRO", "DESK", "three flat stacks side by side on a dark wooden table: a tall red stack, a short orange stack and a very tall blue stack, no text and no digits.",
   "A credit card, a personal loan, and a car loan. Together they add up to forty thousand dollars.")
sc("CLOSE", "KNIGHT", "his face in close-up, eyes wide, mouth slightly open, a cold blue glow from below the frame.",
   "Your stomach drops. This is not one reckless purchase. It is years of small yeses, with interest on top.")
sc("SIT", "OFFICE", "he sits at his cubicle with a forced smile, two small coworker silhouettes behind him chatting with a beach icon floating above them.",
   "At work, nobody talks about debt. They talk about vacations, and you smile along while your chest tightens.")
sc("HAND", "OFFICE", "a hand holding a printed statement made of gray blurred lines with one large red upward arrow icon at the bottom, no readable text and no digits.",
   "The credit card statement shows an interest charge so large that you read it three times.")
sc("MACRO", "DESK", "a flat illustration of a credit card with a red upward arrow and a stack of coins slipping away from it, no text and no digits.",
   "That card charges about twenty-four percent a year, roughly two hundred forty dollars a month in interest alone.")
sc("CLOSE", "KNIGHT", "his face in close-up, jaw tight, a thin line of cold light across his eyes.",
   "Your minimum payment is three hundred sixty dollars, so only about one hundred twenty actually reduces the debt.")
sc("SIT", "KNIGHT", "he sits at the kitchen table looking at the camera, a drawn icon of a small machine with a red arrow floating beside his head.",
   "You realize the card is not just a balance. It is a machine that quietly works against you.")
sc("HAND", "KDAY", "a hand holding a pen over an open notebook, three rows of small colored dots drawn on the page, no letters and no digits.",
   "So you sit down with a notebook and list every debt, every rate, and every minimum payment.")
sc("MACRO", "DESK", "an open notebook with three rows of colored bars and small coin icons beside a plain gray floor line, no readable text and no digits.",
   "The three minimums add up to nine hundred ten dollars a month. That is the floor, not the plan.")
sc("SIT", "LIVING", "he sits on the couch with the notebook open on his knees and a pencil behind his ear, a worried but determined look, a floor lamp glowing.",
   "You take home about thirty-nine hundred dollars a month, and rent, food, and bills already take most of it.")
sc("HAND", "KNIGHT", "a hand drawing a line through small icons of a delivery bag, a subscription card and a pair of headphones in a notebook, no letters and no digits.",
   "You go through your spending and find about two hundred ninety dollars a month that was not doing much for you.")
sc("MACRO", "DESK", "a flat illustration of a small coin stack joining a larger coin stack with an arrow, a red debt stack shrinking behind them, no text and no digits.",
   "Add that to the minimums, and you can send twelve hundred dollars a month at your debt.")
sc("STAND", "KDAY", "he stands at the refrigerator taping a hand-drawn paper chart with three colored horizontal bars, red, orange and blue, on it, a roll of tape in his other hand.",
   "You draw three colored bars on paper and tape it to the refrigerator, where you cannot avoid it.")

# ---- acto 3: los años del medio ----
sc("SIT", "KDAY", "he sits at the kitchen table with a pencil to his chin, two floating icons beside his head: a mountain and a small snowball.",
   "Now comes a question people argue about like a sport. Which debt do you attack first?")
sc("MACRO", "DESK", "a flat illustration of a large tall mountain made of red coin stacks with a single arrow striking its highest peak, no text and no digits.",
   "One method is the avalanche. You send every extra dollar to the debt with the highest interest rate.")
sc("MACRO", "DESK", "a flat illustration of a small snowball rolling downhill and growing larger, with a tiny flag at the bottom, no text and no digits.",
   "The other is the snowball. You pay off the smallest balance first, for quick wins that keep you motivated.")
sc("CLOSE", "KNIGHT", "his face in close-up, one eyebrow raised as he compares two options, a faint blue light on his cheek.",
   "In this example, the avalanche finishes about a month sooner and saves roughly eleven hundred dollars of interest.")
sc("SIT", "LIVING", "he sits on the couch with open hands in a balanced gesture, a small icon of two scales floating beside his head.",
   "That is not a huge gap. The best method is the one you will actually stick with.")
sc("HAND", "KNIGHT", "a hand circling the red bar on a notebook page with a pen, the orange and blue bars left plain, no letters and no digits.",
   "You like numbers, so you choose the avalanche. The twenty-four percent card goes first, and the rest get minimums.")
sc("STAND", "KDAY", "he stands at the kitchen counter tapping a smartphone, a small calendar icon with a loop arrow floating beside the screen, morning light.",
   "You set up automatic payments, so willpower is no longer part of the plan.")
sc("WIDE", "STREET", "a quiet suburban street where a large glossy black SUV pulls into a driveway on the right, Sam tiny on the sidewalk at the left holding a grocery bag.",
   "Meanwhile your neighbor pulls up in his glossy black SUV, and you feel that old pinch of comparison.")
sc("CLOSE", "STREET", "his face in close-up, a calm effort at a smile, a blurred black car behind him at dusk.",
   "You remind yourself that you do not know how he pays for it, and it is not your race.")
sc("HAND", "LIVING", "a hand holding a smartphone, the screen shows a group chat with palm tree icons and gray bubbles, no readable text and no digits.",
   "A coworker invites you on a weekend trip. You say maybe, then no, then offer a picnic instead.")
sc("SIT", "KDAY", "he sits at the kitchen table with a mug, a slight nervous smile, warm morning light.",
   "It feels awkward to say it out loud, but nobody is angry. Most people have been where you are.")
sc("MACRO", "DESK", "a flat illustration of a paper chart with a red bar slightly shorter than before, a small red marker lying beside it, no text and no digits.",
   "Month by month, the red bar on the refrigerator chart gets a little shorter.")
sc("HAND", "KDAY", "a hand coloring over a section of a long bar on a paper chart with a red marker, small flecks of marker dust, no letters and no digits.",
   "Every payday you color in a small piece. It looks silly, and it works better than any app.")
sc("WIDE", "OFFICE", "a wide view of the open office with Sam small at his cubicle, a tall stack of paperwork on one side and a small green arrow icon above the monitor.",
   "At work you take on extra tasks, earn a small raise, and send most of it to the card.")
sc("CLOSE", "OFFICE", "his face in close-up looking tired but steady, soft office light.",
   "It is slow. Some days you feel like you are bailing out a boat with a spoon.")
sc("STAND", "STREET", "he stands in a driveway beside his plain older sedan with the hood open and a thin wisp of pale smoke rising, hands on his head.",
   "In month ten, your car needs an expensive repair. Your stomach drops again, and the old temptation whispers.")
sc("MACRO", "DESK", "a small glass jar of coins with a flat shield icon on it beside a plain wrench, on a dark wooden table, no letters and no digits.",
   "Luckily you built a small cash cushion first, so the repair does not go back on the card.")
sc("SIT", "LIVING", "he sits on the couch with a relieved expression, the small jar of coins resting on his knee, evening light.",
   "You pay with the cushion and start rebuilding it right away. Setbacks happen, and a plan has room for them.")
sc("HAND", "KNIGHT", "a hand holding a smartphone, the screen shows three pale bars and a small red arrow nudging up, no readable text and no digits.",
   "Without that cushion, the repair would have landed on the twenty-four percent card, and the climb would restart.")
sc("CLOSE", "KNIGHT", "his face in close-up at night, eyes tired, lamp light on one side.",
   "There are nights you doubt this. You wonder if you are wasting your twenties on spreadsheets.")
sc("SIT", "KDAY", "he sits at the kitchen table in morning light with the fridge chart visible behind him, the bars clearly shorter, a soft smile returning.",
   "Then you look at the chart on the refrigerator and notice the bars really are getting shorter.")
sc("MACRO", "DESK", "a flat illustration of a very long winding gray path with small clock icons along it and a faint flag far in the distance, no text and no digits.",
   "Paying only the minimums would take roughly five and a half years, with about fourteen thousand dollars in interest.")
sc("MACRO", "DESK", "a flat illustration of a shorter straight green path with one clock icon along it and a flag close by, no text and no digits.",
   "With your plan it takes about three years and four months, and the interest drops to under eight thousand dollars.")
sc("CLOSE", "LIVING", "his face in close-up, a quiet nod, warm light.",
   "That difference is more than six thousand dollars. It is a holiday, a down payment, or an emergency fund.")
sc("SIT", "KDAY", "he sits at the kitchen table, hands open in a calm gesture, a small cloud icon with a sun behind it floating beside his head.",
   "These numbers are only an illustration, and rates change. Still, one thing holds. Interest is the price of waiting.")

# ---- acto 4: el giro / la prueba ----
sc("HAND", "KDAY", "a hand coloring the very last piece of the long red bar on the paper chart so it is completely filled in, a red marker in the fingers, morning light.",
   "In month twenty-four, the red bar finally disappears. The twenty-four percent card is gone.")
sc("CLOSE", "KDAY", "his face in close-up, calm, almost surprised, a very small smile.",
   "You do not feel triumphant. You feel quiet, like a loud machine in the next room finally shut off.")
sc("STAND", "KDAY", "he stands at the kitchen counter holding the blue credit card in one hand and scissors in the other, about to cut, steady hands.",
   "You cut the card in two with scissors, mostly because you want to see it happen.")
sc("MACRO", "DESK", "a flat illustration of the red bar disappearing while its coin stack flows into the orange bar, a green arrow beside them, no text and no digits.",
   "Now every dollar that used to feed the card rolls into the next debt. The pace speeds up.")
sc("SIT", "LIVING", "he sits on the couch with the notebook and a warm slight smile, a small flat icon of an orange bar crossed out beside his head.",
   "Four months later the personal loan is gone too. Only the car loan remains, and it charges far less.")
sc("WIDE", "STREET", "an evening street with Sam walking small along the sidewalk, the neighbor silhouette beside the black SUV in the driveway at the edge of the frame.",
   "One evening you pass the neighbor with the black SUV, and he asks how you are doing.")
sc("STAND", "STREET", "he stands on the sidewalk with open hands, calm, the black SUV large at the right edge of the frame.",
   "You tell him you are almost debt free, and he nods slowly, like someone doing a hard sum.")
sc("CLOSE", "STREET", "his face in close-up, gentle and a little sad, dusk light and the shadow of a black car behind him.",
   "He admits he is behind on his payments. Debt is quiet like that. It sits at many dinner tables.")
sc("HAND", "KNIGHT", "a hand pushing a notebook page across a kitchen table toward the edge of the frame, three colored bars drawn on the page, no letters and no digits.",
   "You do not preach. You only say that a plan is better than hoping, and he thanks you.")
sc("SIT", "KDAY", "he sits at the kitchen table with a small slice of cake on a plate and a fork, a small smile, a window of warm light behind him.",
   "In the last year you allow small rewards, like a nice dinner when each bar shrinks.")
sc("MACRO", "DESK", "a flat illustration of a small gift icon beside a small shield icon on a dark wooden table, no text and no digits.",
   "Progress needs celebration, or it feels like punishment. The trick is to keep the celebrations small.")
sc("HAND", "KDAY", "a hand holding a smartphone toward the camera with a plain pale screen and one small green circle, no readable text and no digits.",
   "In month forty, you make the last payment. You hold your phone and wait for something dramatic.")
sc("CLOSE", "KDAY", "his face in close-up, calm, a slow blink, soft light.",
   "Nothing dramatic happens. And that is exactly the point. Freedom is often quiet.")
sc("WIDE", "KDAY", "he stands small beside the refrigerator lifting the paper chart from its tape, the empty paper white and clean, sunny window light.",
   "You take down the paper chart from the refrigerator. It has done its job.")
sc("STAND", "KDAY", "he stands at the kitchen table in soft evening light, the two halves of the blue card and the scissors resting on the table in front of him.",
   "And so we are back at the kitchen table, with a cut card and a calm evening.")

# ---- cierre ----
sc("SIT", "KDAY", "he sits at the kitchen table looking at the camera with a warm, calm expression, a mug and a notebook in front of him.",
   "So here is your point of view. You do not need a perfect salary to leave debt behind.")
sc("MACRO", "DESK", "an open notebook with three colored bars and three small dots, a pen resting on the page, no letters and no digits.",
   "Step one, list every debt with its balance, its rate, and its minimum, so nothing hides from you.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of a calendar with a loop arrow, no readable text and no digits.",
   "Step two, pick a method, the avalanche or the snowball, and automate the extra payment.")
sc("MACRO", "DESK", "a small glass jar of coins with a flat shield icon beside a notebook on a dark wooden table, no letters and no digits.",
   "Step three, keep a small cushion for surprises, so one bad month does not undo your progress.")
sc("STAND", "KDAY", "he stands at the refrigerator with a red marker, the paper chart with three colored bars taped in front of him, an upbeat posture.",
   "Track it somewhere you can see, and celebrate small wins. Slow, steady progress still gets you there.")
sc("SIT", "CLEAN", "He sits at a table looking at the camera with a friendly smile; floating at the right next to his head, a large flat icon of a red subscribe button with a bell, thick outline, no text.",
   "If this story made you think about your own debt, subscribe, and come back for the next quiet story.")
sc("MACRO", "DESK", "a closed notebook with a pen on top and a hand-drawn shield icon on the cover, on a dark wooden table, no letters and no digits.",
   "This video is for education only, not financial advice. Rates, expenses and risks differ for everyone, so speak with a licensed professional about your own situation.")
sc("WIDE", "STREET", "he walks home along a quiet street in the evening with relaxed shoulders, small in the frame, a long warm sunset behind him.",
   "You walk home with lighter shoulders. The monthly money that once went to lenders now belongs to you.")
sc("MACRO", "DESK", "two halves of a plain blue credit card on a dark wooden table beside a small pair of scissors, soft morning light, no letters and no digits.",
   "The card is in two pieces. You are in one.")

if __name__ == "__main__":
    emit(S, "v6", "Video 6: POV: You Cleared $40,000 of Debt on a Normal Salary - Step by Step")
