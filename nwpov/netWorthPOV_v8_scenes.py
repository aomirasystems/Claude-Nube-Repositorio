"""
Net Worth POV - Video 8: "POV: You Got a Raise and Kept Your Life the Same - On Purpose"
Cifras ilustrativas: aumento neto 800/mes (12,000 brutos/año); reparto 600 inversion + 200 disfrute; 600/mes x 120 meses a 6% anual (0.5%/mes) -> ~98,300; vecino compromete 800/mes en pagos nuevos x 60 meses = 48,000; recorte de ingreso de 800/mes = pausa de la inversion unos meses.
Uso: python netWorthPOV_v8_scenes.py
"""
from nwpov_common import emit

S = []
def sc(kind, setting, visual, narr):
    S.append((kind, setting, visual, narr))

# ---- gancho ----
sc("MACRO", "DESK", "a chipped blue ceramic coffee mug with a thin curl of steam on a dark wooden table, a closed laptop beside it, no letters and no digits.",
   "A chipped blue coffee mug sits beside a laptop. You have had it for eleven years.")
sc("SIT", "OFFICE", "he sits at his cubicle desk with the chipped blue mug in one hand, looking at a glowing monitor, a calm expression, a quiet morning office.",
   "It is Monday morning, and an email just arrived with the words you have waited two years to read.")
sc("HAND", "OFFICE", "a hand resting on a laptop keyboard, the screen shows a flat green upward arrow icon and gray blurred bars, no readable text and no digits.",
   "Your salary is going up by about twelve thousand dollars a year, starting next month.")
sc("CLOSE", "OFFICE", "his face in close-up, a soft private smile, eyes calm, the glow of the screen on his cheek.",
   "You smile, but you do not celebrate. You close the laptop and quietly finish your coffee.")
sc("STAND", "OFFICE", "he stands by a break room counter with the chipped mug while three coworker silhouettes cropped at the edge gesture toward a car icon, a plane icon and a watch icon floating in the air.",
   "At lunch, coworkers say you should treat yourself, and they list the car, the trip, and the watch.")
sc("SIT", "OFFICE", "he sits at a small table with a plain sandwich in a paper wrapper, a patient smile, coworker silhouettes laughing at the edge of the frame.",
   "You nod and order the same sandwich as always, because you already know what this raise is for.")
sc("WIDE", "STREET", "a suburban street at golden hour with a large glossy black SUV in a very big driveway on the right, Sam tiny on the sidewalk at the left.",
   "On the way home, your neighbor waves from a brand new black SUV and a very large driveway.")
sc("MACRO", "CLEAN", "a large flat icon of two left-pointing arrows in a rewind symbol, thick dark outline, centered on a plain cream wall, no text.",
   "So let us rewind to how you learned what to do with a raise.")

# ---- acto 2: el punto de partida ----
sc("WIDE", "KDAY", "a wide view of a sunny kitchen with Sam small at the table, a bag of shopping and a new jacket on a chair, a bright window behind him.",
   "Six years earlier, you get your first meaningful raise, and it feels like a bonus from the universe.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a pale banking app with a small green arrow and gray bars, no readable text and no digits.",
   "For three months the extra money lands in your account, and you tell yourself you will plan it soon.")
sc("MACRO", "DESK", "a flat illustration of a trail of tiny coins leaking away from a small stack toward a coffee cup, a gadget and a subscription card, no text and no digits.",
   "But money without a job wanders. A coffee, a gadget, a subscription, and it quietly disappears.")
sc("CLOSE", "KNIGHT", "his face in close-up at night, a sinking, surprised expression, a cold glow from below the frame.",
   "By December you check your savings and realize the raise has changed nothing, except the size of your bills.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a notebook and a pen, a firm determined look, one lamp glowing.",
   "That is the day you decide the next raise will have a job before it arrives.")
sc("HAND", "KNIGHT", "a hand writing a single short line at the top of a notebook page, followed by a simple drawn arrow, no letters and no digits.",
   "You write a simple rule in your notebook. Every raise gets split before it ever touches daily spending.")
sc("MACRO", "DESK", "a flat illustration of a notebook page showing one very long colored bar and one short colored bar side by side, a small shield icon beside the long bar and a small gift icon beside the short bar, no text and no digits.",
   "Most goes to the future. A smaller part goes to enjoying your life. Nothing goes to guessing.")
sc("CLOSE", "OFFICE", "his face in close-up, reading a message on a screen with a quiet focus, soft office light.",
   "Five years later, the email arrives. After taxes, the raise is about eight hundred dollars a month.")
sc("MACRO", "DESK", "a flat illustration of a small coin stack with a bold arrow growing it larger, a calm green glow behind it, no text and no digits.",
   "Eight hundred dollars sounds small and feels huge. It is the difference between a tight month and a comfortable one.")
sc("HAND", "KDAY", "a hand opening a notebook to a page with a long bar and a short bar drawn side by side, a pen in the other hand, no letters and no digits.",
   "You open the notebook and apply your rule. Six hundred dollars goes to investing, and two hundred is for living.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a small plant, no readable text and no digits.",
   "You set up the transfer for payday, before the money has any chance to start feeling like yours.")
sc("SIT", "KDAY", "he sits at the kitchen table with a mug in morning light, relaxed shoulders, a small calendar icon with a loop arrow floating beside his head.",
   "That way the decision is made once, on a calm morning, instead of fifty small times a month.")
sc("MACRO", "DESK", "a flat illustration of a small gift icon, a ticket icon and a pair of hiking boots drawn side by side, no text and no digits.",
   "The two hundred dollars is not guilt money. It is real fun money, and you promise to enjoy every cent.")
sc("SIT", "LIVING", "he sits on the couch with the chipped mug, quiet and content, a plain beige couch with no new cushions, a floor lamp glowing.",
   "You tell no one. There is no announcement, no party, no new couch, and no new phone either.")
sc("CLOSE", "LIVING", "his face in close-up, a thoughtful half smile and a hint of longing in the eyes, warm lamp light.",
   "Inside, there is a small pang. The old temptation is still there, just quieter.")

# ---- acto 3: los años del medio ----
sc("WIDE", "STREET", "a suburban street where the neighbor silhouette stands proudly in his driveway beside a large glossy black SUV, Sam tiny at his front door across the street.",
   "Across the street, your neighbor gets a raise the same month, and his response looks very different.")
sc("STAND", "STREET", "he stands on the sidewalk looking toward a bigger, shinier black SUV in the neighbor's driveway, the neighbor silhouette cropped at the edge, golden hour light.",
   "Within weeks a bigger black SUV appears in his driveway, shiny and loud, with a monthly payment to match.")
sc("SIT", "LIVING", "he sits on the couch looking at the camera with a gentle, non-judging expression, a small coin icon with a red arrow floating beside his head.",
   "You do not judge him. You just notice that his raise was spent before it arrived.")
sc("HAND", "KDAY", "a hand holding a pair of simple hiking boots by the laces, a small sun icon in the corner, no letters and no digits.",
   "Your two hundred dollars of fun money becomes a weekend hike, new boots, and a lot of cheap joy.")
sc("CLOSE", "KDAY", "his face in close-up, a genuine relaxed smile, fresh morning light.",
   "You are not living like a monk. You are simply choosing a few things that matter to you.")
sc("WIDE", "OFFICE", "a wide view of the office with Sam small at his cubicle holding his old chipped mug while two coworker silhouettes point toward his worn laptop bag and smile.",
   "At work, a few people tease you about the old mug and the old laptop bag.")
sc("SIT", "OFFICE", "he sits at his cubicle with a calm smile and open palms, a coworker silhouette cropped at the edge, a small shield icon floating above his desk.",
   "You tell them the raise is already spent. They ask on what, and you say, on later.")
sc("MACRO", "DESK", "a flat illustration of an arrow moving from a wallet to a green plant in a plain pot, a small calendar icon with a loop arrow beside it, no text and no digits.",
   "Every month, six hundred dollars moves into a plain, low cost index fund, and it never asks for attention.")
sc("SIT", "KNIGHT", "he sits at the kitchen table in the evening reading a book drawn as plain gray lines, a mug beside him, a relaxed face.",
   "Some months you forget it exists. That is the point. The best habits feel almost invisible, and very easy to keep.")
sc("HAND", "KNIGHT", "a hand holding a smartphone, the screen shows a pale line chart rising gently with a small green dot, no readable text and no digits.",
   "A year passes, and you check the account. It is not dramatic, but it is real, and it is yours.")
sc("MACRO", "DESK", "a flat illustration of a green line chart starting low and bending slowly upward, a small clock icon at the base, no text and no digits.",
   "In this example, the account earns about six percent a year, and the line grows slowly at first.")
sc("WIDE", "STREET", "the neighbor's driveway with the large black SUV and now a small boat on a trailer beside it, Sam tiny on the sidewalk in the foreground.",
   "Meanwhile your neighbor adds a boat trailer to the driveway, and a second payment to the bills.")
sc("CLOSE", "STREET", "his face in close-up, gentle and a little sympathetic, the blurred black SUV and the boat behind him at dusk.",
   "He is not a bad person. He simply believes the future will always pay for the present.")
sc("SIT", "KDAY", "he sits at the kitchen table with a mug and the notebook, a quiet thoughtful look, morning light.",
   "Every few months you ask yourself a quiet question. What would I regret in ten years?")
sc("HAND", "LIVING", "a hand holding the gray notebook closed on his lap, the other hand resting on the couch arm, soft evening light.",
   "Mostly it is not the dinners or the trips you would regret. It is the year you never started.")
sc("MACRO", "DESK", "a flat illustration of a car icon with a red downward arrow beside a stack of coins slowly shrinking, a tiny clock icon behind them, no text and no digits.",
   "The math is simple. Eight hundred dollars a month in new payments adds up to forty-eight thousand dollars in five years.")
sc("HAND", "DESK", "a hand pointing a pen at a shiny car drawn smaller and smaller in three steps on a notebook page, a red downward arrow beside it, no text and no digits.",
   "That buys a car that loses value every year, and a bigger life that costs more to keep.")
sc("MACRO", "DESK", "a flat illustration of a green plant growing from a coin stack into a tall tree with a small flag on top, a faint clock icon behind it, no text and no digits.",
   "Now look at your six hundred dollars. Invested monthly for ten years at about six percent, it becomes roughly ninety-eight thousand.")
sc("CLOSE", "LIVING", "his face in close-up, calm and a bit wistful, warm lamp light on one cheek.",
   "Same raise. Same city. Two very different futures, built from one boring decision made on one calm morning.")
sc("SIT", "LIVING", "he sits on the couch with open hands, a small icon of a cloud and a sun floating beside his head.",
   "Of course, this is an illustration. Returns vary, and some years the market will test your patience.")
sc("STAND", "STREET", "he stands in the neighbor's front yard at golden hour with a paper plate in hand, a cropped silhouette of the neighbor at a grill at the edge of the frame, smoke drifting.",
   "In year three, your neighbor invites you to a barbecue, and you go, and it is honestly a very good time.")
sc("CLOSE", "STREET", "his face in close-up, warm and amused, soft smoke haze behind him.",
   "You realize you like him, and that nothing about this plan requires being better than him.")
sc("SIT", "KDAY", "he sits at the kitchen table with a small glass jar of coins with a flat shield icon, a calm smile.",
   "You also keep a small cash cushion, so a surprise bill does not force you to stop investing.")
sc("HAND", "KDAY", "a hand placing a coin into the small glass jar with the shield icon, soft morning light.",
   "Because a plan that survives bad weeks is worth more than a perfect plan that breaks.")
sc("SIT", "KDAY", "he sits at the kitchen table looking toward the window, where gray clouds have started to gather, a mug held in both hands.",
   "And then, in year six, the weather really does turn.")

# ---- acto 4: el giro / la prueba ----
sc("WIDE", "OFFICE", "a wide view of the office with silhouettes at cubicles slumped under small gray cloud icons, Sam small at his desk, the lighting dimmer.",
   "Your company has a rough year. Raises are frozen, hours are cut, and the mood in the office turns very heavy.")
sc("CLOSE", "OFFICE", "his face in close-up, quietly absorbing bad news, dim office light.",
   "Your take home pay drops by about eight hundred dollars a month. The same amount as your last raise.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with the notebook open and a steady breath, one lamp glowing.",
   "You feel your stomach tighten. Then you open the notebook and realize that you still have plenty of room.")
sc("HAND", "KNIGHT", "a hand holding a smartphone, the screen shows the loop arrow icon with a small pause symbol on it, no readable text and no digits.",
   "You pause the six hundred dollars of investing for a few months, and your living costs do not change.")
sc("MACRO", "DESK", "a flat illustration of a coin stack with a small pause icon beside it and a tidy green check, no text and no digits.",
   "Because the raise never became a fixed bill, losing it is a pause, not an emergency.")
sc("WIDE", "STREET", "the neighbor's driveway at night with the black SUV and the boat, the neighbor silhouette sitting on the curb with his head in his hands, Sam tiny at his own door.",
   "Across the street, your neighbor is not so lucky. His payments do not pause when his hours do.")
sc("CLOSE", "STREET", "a cropped silhouette of the neighbor at the edge of the frame lit by a phone, the dark SUV beside him, Sam's concerned face in the foreground.",
   "You see him in the driveway at night, staring at his phone, with the glow of the SUV beside him.")
sc("STAND", "STREET", "he walks across the street at dusk toward the neighbor silhouette sitting on the curb, a friendly open posture, the black SUV large in the background.",
   "You walk over, say hello, and do not mention the numbers. He admits things are tight.")
sc("SIT", "LIVING", "he sits on the couch beside a neighbor silhouette with two mugs on the table, leaning in gently, a patient expression.",
   "You do not lecture him. You tell him what worked for you, and what did not work at all.")
sc("HAND", "LIVING", "a hand handing over a set of car keys to another hand at the edge of the frame, a small relieved sun icon in the corner.",
   "In the end, he sells the SUV, and for the first time in years he finally sleeps well.")
sc("MACRO", "DESK", "a flat illustration of a pause icon changing back into a play arrow beside a coin stack, a small green plant sprouting next to it, no text and no digits.",
   "The pause on your side lasts only a few months. Then you restart the transfer, quietly.")
sc("SIT", "KDAY", "he sits at the kitchen table in warm morning light looking at the camera, a small clock icon floating beside his head, a calm slight smile.",
   "Even with that pause, the picture stays similar. Time and consistency do most of the work.")
sc("WIDE", "OFFICE", "a wide view of the office on a quiet Monday morning with Sam small at his cubicle holding the chipped blue mug, soft sunlight.",
   "And so we return to that Monday morning, with the email and the chipped mug.")
sc("SIT", "OFFICE", "he sits at his cubicle looking at the camera with a gentle smile, the chipped mug beside the keyboard.",
   "You are not smarter than anyone. You just decided early, and calmly, what each new dollar would do.")
sc("CLOSE", "OFFICE", "his face in close-up, sincere, a faint glow of light on his cheek.",
   "A raise is a rare chance to choose your future before your habits choose it for you.")

# ---- cierre ----
sc("SIT", "KDAY", "he sits at the kitchen table looking at the camera with a warm, calm expression, a mug and a notebook in front of him.",
   "So here is your point of view. A raise does not have to change your life to improve it.")
sc("MACRO", "DESK", "an open notebook with a long bar and a short bar drawn side by side and a pen resting on the page, no letters and no digits.",
   "Step one, decide before the raise arrives what each new dollar will do, and write it down.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a plant, no readable text and no digits.",
   "Step two, automate the biggest share on payday, so the future is paid first.")
sc("MACRO", "DESK", "a flat illustration of a small gift icon and a ticket icon beside a tiny jar, warm light, no text and no digits.",
   "Step three, keep a small share for enjoying life now, so the plan feels kind and lasts.")
sc("STAND", "KDAY", "he stands in the kitchen in morning light with a mug, calm and steady, a small shield icon floating over the window.",
   "And keep your fixed bills low, because flexibility is the quiet luxury behind every calm month.")
sc("SIT", "CLEAN", "He sits at a table looking at the camera with a friendly smile; floating at the right next to his head, a large flat icon of a red subscribe button with a bell, thick outline, no text.",
   "If this story made you think about your next raise, subscribe, and come back for the next quiet story.")
sc("MACRO", "DESK", "a closed notebook with a pen on top and a hand-drawn shield icon on the cover, on a dark wooden table, no letters and no digits.",
   "This video is for education only, not financial advice. Rates, expenses and risks differ for everyone, so speak with a licensed professional about your own situation.")
sc("WIDE", "STREET", "he walks home along a quiet street in the evening past a large driveway with an empty space where the SUV used to be, small and relaxed, a warm sunset behind him.",
   "You walk home past the big driveway, and you do not feel behind. You feel steady.")
sc("MACRO", "DESK", "the chipped blue coffee mug on a dark wooden table beside a closed notebook, soft morning light, no letters and no digits.",
   "The mug is chipped. The month is calm.")

if __name__ == "__main__":
    emit(S, "v8", "Video 8: POV: You Got a Raise and Kept Your Life the Same - On Purpose")
