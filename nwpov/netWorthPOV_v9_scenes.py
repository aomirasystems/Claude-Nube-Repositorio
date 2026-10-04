"""
Net Worth POV - Video 9: "POV: You Lost 30% in a Market Crash - And Did Nothing"
Cifras ilustrativas: saldo 100,000; mercado cae 30% en 12 meses (precio 1.00 -> 0.70) y vuelve a 1.00 en 24 meses mas; aporte 500/mes. Fondo: ~75,100 (con aportes). Quien mantiene -> ~121,400 al mes 36; quien vende en el fondo y vuelve cuando el precio regresa (ahorra 500/mes en efectivo) -> ~87,100; brecha ~34,000. Perdida de 30% requiere ganancia de 1/0.7 - 1 = 42.9%.
Uso: python netWorthPOV_v9_scenes.py
"""
from nwpov_common import emit

S = []
def sc(kind, setting, visual, narr):
    S.append((kind, setting, visual, narr))

# ---- gancho ----
sc("MACRO", "DESK", "a smartphone lying face down on a dark wooden table beside a white mug of tea with a thin curl of steam, a small index card with a hand-drawn shield icon leaning against the mug, no letters and no digits.",
   "A phone lies face down on the kitchen table, beside a mug of tea that is slowly going cold.")
sc("SIT", "KDAY", "he sits at the kitchen table on a gray autumn morning with a mug of tea, a calm face, rain streaks on the window behind him.",
   "It is a Wednesday in October, and every news channel is shouting. The market has fallen again this week, and again.")
sc("WIDE", "LIVING", "a wide view of the living room with a television showing a large red downward arrow tumbling along a chart, a news anchor silhouette with a stern posture, Sam small in the doorway.",
   "In the living room, the television shows a red arrow falling down a chart, and anchors with very serious faces.")
sc("CLOSE", "KDAY", "his face in close-up, steady and quiet, a slow breath, soft gray window light.",
   "Your account has lost about thirty percent from its peak. You know it, and you are not checking.")
sc("HAND", "KDAY", "a hand reaching toward a smartphone lying face down on the table, then pausing and turning toward the mug of tea instead.",
   "You reach for the phone, then you stop, and you pour yourself some more tea instead.")
sc("SIT", "KDAY", "he sits at the table sipping tea with half-closed eyes, a small silhouette of a crowd of people running drawn on the window behind him as a faint drawing.",
   "Somewhere right now, millions of people are selling everything, with shaking hands. You are not one of them.")
sc("CLOSE", "KDAY", "his face in close-up, a small honest half smile, eyes steady.",
   "You are not brave. You are not a genius. You simply wrote the rules long before the storm.")
sc("MACRO", "CLEAN", "a large flat icon of two left-pointing arrows in a rewind symbol, thick dark outline, centered on a plain cream wall, no text.",
   "So let us rewind to the day you wrote those rules.")

# ---- acto 2: el punto de partida ----
sc("SIT", "KDAY", "he sits at the kitchen table with a smartphone held close to his face, wide eager eyes, a bowl of cereal beside him, morning light.",
   "Nine years earlier, you open your first investment account, and you check it every single morning.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen alternates between a pale green arrow and a pale red arrow drawn side by side, no readable text and no digits.",
   "When the number is green, you feel clever. When it is red, you feel sick.")
sc("CLOSE", "KNIGHT", "his face in close-up at night, a queasy worried look, a cold blue glow from below the frame.",
   "In the second year, the market dips about ten percent, and your stomach drops every time you look.")
sc("HAND", "KNIGHT", "a thumb hovering over a large flat red sell button icon on a smartphone, no readable text and no digits, a dark kitchen around it.",
   "One night you open the app, find the sell button, and your thumb hovers over it for a long minute.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with his head in his hands, a smartphone face up on the table, a single lamp glowing.",
   "You do not press it, but only because you are tired. It scares you how close you came.")
sc("STAND", "OFFICE", "he stands near a break room counter while an older coworker silhouette cropped at the edge hands him a paper cup of coffee, a concerned friendly posture.",
   "The next day, an older coworker notices your face and asks what is wrong. You admit you almost sold.")
sc("SIT", "OFFICE", "he sits at a small table with the older coworker silhouette across from him, the coworker's hands open in a calm gesture, a gentle rising green line drawn in the air between them.",
   "He says markets have fallen many times before, and each time they eventually recovered, though never on a schedule.")
sc("CLOSE", "OFFICE", "his face in close-up, listening hard, a faint furrow between his eyebrows.",
   "That last part matters. Eventually is not a date, so you must be able to wait.")
sc("MACRO", "DESK", "a flat illustration of two vertical bars on a dark wooden table: a tall bar and a shorter bar with a thin red segment missing from its top, no text and no digits.",
   "He shows you a small trick. A thirty percent loss does not need a thirty percent gain to recover.")
sc("MACRO", "DESK", "a flat illustration of a short bar with a long green arrow climbing alongside it to the height of a taller bar, no text and no digits.",
   "It needs about forty-three percent, because you are climbing back from a smaller number.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night writing on a small plain index card with a pen, one lamp glowing, a calm resolute face.",
   "You go home and write rules on an index card, while you are calm and the market is quiet.")
sc("HAND", "KDAY", "a hand holding a small index card covered in three simple hand-drawn icons: a calendar with a single check, a hand stopping a red sell button, and a loop arrow, no letters and no digits.",
   "Rule one, check the balance only once a month. Rule two, do not sell because of fear.")
sc("MACRO", "DESK", "a flat illustration of an index card with a loop arrow icon and a small coin stack, a pen lying beside it, no text and no digits.",
   "Rule three, keep the automatic monthly deposit running, especially when it feels uncomfortable.")
sc("STAND", "KDAY", "he stands at the kitchen counter taping the small index card to the inside of an open kitchen cabinet next to the mugs, a roll of tape in his hand.",
   "You tape the card inside a kitchen cabinet, where you will see it every time you reach for a mug.")
sc("SIT", "KDAY", "he sits at the kitchen table with a mug, a gentle self-aware smile, the open cabinet door showing the index card behind him.",
   "It feels silly, writing instructions to your future self. But future you is exactly who needs them.")

# ---- acto 3: los años del medio ----
sc("WIDE", "STREET", "a wide view of the neighborhood across several seasons with the sun and moon icons and a gently wobbling green line drawn across the sky, Sam tiny on the sidewalk.",
   "Years pass, and the market does what it always does. It climbs, it wobbles, and it climbs again.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a plant with a loop arrow, no readable text and no digits.",
   "Every month, five hundred dollars moves automatically into a plain, low cost index fund. You barely notice.")
sc("SIT", "KDAY", "he sits at the kitchen table glancing at his phone briefly with a mug in hand, a calendar icon with a single check floating beside him.",
   "You check once a month, as promised. You nod, you close the app, and you go back to your normal life.")
sc("MACRO", "DESK", "a flat illustration of a medium coin stack with a small green flag on top, a small clock icon behind it, no text and no digits.",
   "By your thirty-eighth birthday, in this example, the account has grown to about one hundred thousand dollars.")
sc("CLOSE", "LIVING", "his face in close-up, quietly proud with a flicker of worry, warm lamp light.",
   "It is the biggest number you have ever owned, and it feels both exciting and fragile.")
sc("WIDE", "STREET", "a suburban driveway where the neighbor silhouette stands beside a large glossy black SUV gesturing excitedly with a smartphone in his hand, Sam tiny on the sidewalk listening.",
   "Your neighbor with the black SUV loves talking about the market. He checks it daily, like a sport.")
sc("STAND", "STREET", "he stands on the sidewalk with a polite listening smile, the neighbor silhouette cropped at the edge, a small sparkling star icon above the neighbor's phone.",
   "He tells you about hot picks and perfect timing, and you listen politely and change nothing.")
sc("SIT", "LIVING", "he sits on the couch with a newspaper drawn as gray lines, a small red downward arrow icon floating beside his head.",
   "Then, one autumn, the first headline appears. Then another. Then a week where everything turns red.")
sc("WIDE", "LIVING", "a wide view of the living room with a television showing a chart falling off a cliff, Sam small on the couch with a blanket, gray autumn light.",
   "The television shows charts falling off a cliff, and experts who agree on nothing except fear.")
sc("CLOSE", "LIVING", "his face in close-up, tight and thoughtful, the red glow of the television on his cheek.",
   "You tell yourself it is just a dip. But the dip keeps going, week after week.")
sc("HAND", "KNIGHT", "a hand holding a smartphone toward the camera, the screen shows a pale chart with a long red downward line, no readable text and no digits.",
   "One night you open the app, against your own rule. The balance is down about twenty percent.")
sc("CLOSE", "KNIGHT", "his face in close-up at night, eyes wide, chest rising sharply, a faint red glow on his cheek.",
   "Your chest tightens. Years of patient work look like they are melting right in front of you.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with his thumb hovering near the phone, a small flat sell button icon floating beside his head, a tired struggling expression.",
   "You feel the old urge, strong and warm and reasonable. Sell now, and stop the pain.")
sc("STAND", "KDAY", "he stands at the open kitchen cabinet in morning light reaching for a mug, the small index card taped inside the door in front of his eyes.",
   "In the morning you reach for a mug, and there it is, the index card in your own handwriting.")
sc("CLOSE", "KDAY", "his face in close-up, reading intently, soft light on one cheek.",
   "Do not check more than once a month. Do not sell because of fear. Keep the deposit running.")
sc("HAND", "KDAY", "a hand holding the index card close to the camera, a thumb on its edge, three simple icons on the card, no letters and no digits.",
   "You read it twice. It is strange how calm your younger self sounds, and how right he turns out to be.")
sc("SIT", "KDAY", "he sits at the kitchen table placing his smartphone face down beside a steaming mug of tea, a quiet determined smile.",
   "You put the phone face down on the table and pour some tea. That is the whole strategy.")
sc("WIDE", "OFFICE", "a wide view of the office with a coworker silhouette standing by his desk with a pale face and a proud lifted chin, Sam small at his own desk.",
   "At work, a coworker announces that he sold everything yesterday. He looks pale and a little proud.")
sc("CLOSE", "OFFICE", "his face in close-up, patient and a little skeptical, soft office light.",
   "He says he will buy back in when things feel safe. You do not ask how he will know.")
sc("STAND", "STREET", "he stands on the sidewalk facing the neighbor silhouette who lifts a triumphant fist beside the large black SUV, golden hour light.",
   "Your neighbor tells you he moved everything to cash, and he says it like a victory.")
sc("CLOSE", "STREET", "his face in close-up, quiet and thoughtful, the blurred black SUV behind him at dusk.",
   "You do not argue. You only wonder when it will ever feel safe enough to return.")
sc("MACRO", "DESK", "a flat illustration of a green line chart falling in a long slope with a small red marker at the bottom, no text and no digits.",
   "The market keeps falling for months. At the bottom, in this example, it is about thirty percent below its peak.")
sc("MACRO", "DESK", "a flat illustration of a tall coin stack shrinking to a shorter coin stack with a small green plus icon at its base, no text and no digits.",
   "Your balance drops from one hundred thousand dollars to roughly seventy-five thousand, even after your monthly deposits.")
sc("HAND", "KNIGHT", "a hand resting on a notebook beside a small stack of coins drawn with a faint empty outline above it, no letters and no digits.",
   "That is twenty-five thousand dollars that looks gone. It is only gone if you sell.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a calm tired smile, a flat price tag icon with a downward arrow floating beside his head.",
   "Meanwhile every deposit buys more shares, at lower prices, like shopping during a very long sale.")

# ---- acto 4: el giro / la prueba ----
sc("MACRO", "DESK", "a flat illustration of a small coin stack turning into a larger pile of simple shares at the bottom of a falling line, a small green arrow beside it, no text and no digits.",
   "In this example, your deposits during the fall quietly buy more shares than they did before the crash.")
sc("CLOSE", "KNIGHT", "his face in close-up, jaw set, the flicker of discomfort still in his eyes.",
   "It still hurts. Doing nothing is not the same as feeling nothing. You feel it all and act on none.")
sc("SIT", "LIVING", "he sits on the couch with a newspaper drawn as gray lines, a tiny green upward arrow icon rising beside his head, morning light.",
   "Slowly, the headlines change. The word crash fades, and the word recovery appears, then the word rally.")
sc("HAND", "LIVING", "a hand holding a smartphone, the screen shows a pale line chart creeping up with small dips, no readable text and no digits.",
   "You check once a month, as your rule says. The balance creeps up, then dips, then creeps up again.")
sc("WIDE", "STREET", "the neighbor silhouette sitting in the black SUV in his driveway with the window up and a faint question-mark icon floating above him, Sam tiny on the sidewalk.",
   "Your neighbor, still in cash, says he is waiting for a calm moment. The market does not send invitations.")
sc("MACRO", "DESK", "a flat illustration of a green line chart climbing slowly back up to the height of its earlier peak with a small flag, no text and no digits.",
   "Prices begin to climb, and in this example, after about two more years, they return to their old peak.")
sc("MACRO", "DESK", "a flat illustration of a tall coin stack with a small green flag on top, taller than the first stack drawn beside it, no text and no digits.",
   "Your account, thanks to the deposits made during the fall, is worth about one hundred twenty-one thousand dollars.")
sc("CLOSE", "LIVING", "his face in close-up, a quiet surprised smile, warm lamp light.",
   "That is more than the old peak, even though the market only returned to its old level.")
sc("HAND", "KDAY", "a hand holding a small stack of coins above a flat sell button icon and a flat clock icon, no letters and no digits.",
   "Now picture your neighbor. He sold near the bottom and waited until prices felt safe again.")
sc("MACRO", "DESK", "a flat illustration of a shorter coin stack with a small gray flag next to the tall green-flag stack, no text and no digits.",
   "In this example, he re-enters after the recovery, with only about eighty-seven thousand dollars to show for it.")
sc("SIT", "LIVING", "he sits on the couch holding open hands, a small flat double arrow icon floating between a tall and a short stack drawn on a notebook beside him.",
   "That is a gap of roughly thirty-four thousand dollars, created by one decision made at the worst moment.")
sc("CLOSE", "KDAY", "his face in close-up, honest and careful, a faint cloud and sun icon floating beside his head.",
   "Remember, this is an illustration. Real recoveries can be faster or slower, and nothing guarantees how it ends.")
sc("SIT", "KDAY", "he sits at the kitchen table looking at the camera with a calm, steady smile, a mug of tea in front of him.",
   "But the pattern is real. People rarely lose the most when the market falls. They lose when they leave.")
sc("WIDE", "STREET", "he walks small along a quiet autumn street with a light rain falling, a warm window glowing behind him, his hands in his pockets.",
   "And so we return to that Wednesday, the phone face down, the tea going cold.")
sc("CLOSE", "KDAY", "his face in close-up, tender and calm, a faint warm light across his eyes.",
   "You did nothing dramatic. You followed an old note, written by someone calm, for someone afraid.")

# ---- cierre ----
sc("SIT", "KDAY", "he sits at the kitchen table looking at the camera with a warm, calm expression, a mug and an index card in front of him.",
   "So here is your point of view. You cannot control the market, but you can control what you do next.")
sc("MACRO", "DESK", "a small index card with three hand-drawn icons, a calendar, a stop hand and a loop arrow, on a dark wooden table, no letters and no digits.",
   "Step one, write your rules while you are calm, and keep them where you will see them.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a plant with a loop arrow, no readable text and no digits.",
   "Step two, automate your deposits, so you keep buying when everyone else is either frozen or running.")
sc("MACRO", "DESK", "a small glass jar of coins with a flat shield icon beside a notebook on a dark wooden table, no letters and no digits.",
   "Step three, only invest money you will not need for years, and keep a cash cushion for emergencies.")
sc("STAND", "KDAY", "he stands at the open kitchen cabinet in morning light with the index card in view, calm and steady, a small shield icon floating over the window.",
   "If the fear is too loud, talk to a licensed professional before you act, not after.")
sc("SIT", "CLEAN", "He sits at a table looking at the camera with a friendly smile; floating at the right next to his head, a large flat icon of a red subscribe button with a bell, thick outline, no text.",
   "If this story helped you think about market storms, subscribe, and come back for the next quiet story.")
sc("MACRO", "DESK", "a closed notebook with a pen on top and a hand-drawn shield icon on the cover, on a dark wooden table, no letters and no digits.",
   "This video is for education only, not financial advice. Rates, expenses and risks differ for everyone, so speak with a licensed professional about your own situation.")
sc("WIDE", "STREET", "he walks along a quiet street in the evening with calm shoulders, small in the frame, a long warm sunset behind him and a few distant gray clouds.",
   "You walk outside, the air is cool, and the world is still loud. You keep your own pace.")
sc("MACRO", "DESK", "a smartphone lying face down on a dark wooden table beside a mug of tea and a small index card, soft morning light, no letters and no digits.",
   "The phone is face down. The plan keeps working.")

if __name__ == "__main__":
    emit(S, "v9", "Video 9: POV: You Lost 30% in a Market Crash - And Did Nothing")
