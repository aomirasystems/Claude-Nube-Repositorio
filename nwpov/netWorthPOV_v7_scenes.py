"""
Net Worth POV - Video 7: "POV: You Started Investing at 35 - And Still Built Something Real"
Cifras ilustrativas: 6% anual, aportes mensuales (tasa mensual 0.5%). Inicia a 25 con 500/mes hasta 65 (480 meses) -> ~995,800; inicia a 35 con 500/mes (360 meses) -> ~502,300; inicia a 35 con 1,000/mes -> ~1,004,500 (aporta 360,000 vs 240,000). A 45: Sam 1,000/mes x 120 meses -> ~163,900; amigo desde los 25 con 500/mes x 240 meses -> ~231,000.
Uso: python netWorthPOV_v7_scenes.py
"""
from nwpov_common import emit

S = []
def sc(kind, setting, visual, narr):
    S.append((kind, setting, visual, narr))

# ---- gancho ----
sc("MACRO", "DESK", "a plain gray notebook with a tiny hand-drawn sprout on its cover resting on a dark wooden table beside a pen, a light layer of dust on the cover, no letters and no digits.",
   "In a drawer sits a gray notebook with a tiny sprout on the cover. Its first page was written late.")
sc("SIT", "LIVING", "he sits on the couch on a quiet Sunday morning holding a smartphone, a mug on the side table, soft sunlight through the window.",
   "You are forty-five, sitting on your couch on a quiet Sunday, and you open your investment account.")
sc("HAND", "LIVING", "a hand holding a smartphone toward the camera, the screen shows a pale line chart climbing steadily with small bumps, no readable text and no digits.",
   "The line has been climbing for ten years. It is not the biggest line anyone has ever seen.")
sc("CLOSE", "LIVING", "his face in close-up, calm and steady, a faint reflection of a pale screen in his eyes.",
   "You feel no rush of triumph. You feel something steadier and quieter, like a floor under your feet.")
sc("HAND", "LIVING", "a hand holding a smartphone, the screen shows a gray message bubble beside a higher green line chart, no readable text and no digits.",
   "A message arrives from your college friend, who started investing at twenty-five. His line is higher than yours.")
sc("SIT", "LIVING", "he sits on the couch with a gentle smile, thumbs on the phone, typing, warm light.",
   "Ten years ago that would have crushed you. Tonight you smile and type back, congratulations.")
sc("CLOSE", "LIVING", "his face in close-up, a relaxed, honest expression, the glow of the phone on his chin.",
   "You finally understand this was never a race against him. It was a race to stop standing still.")
sc("MACRO", "CLEAN", "a large flat icon of two left-pointing arrows in a rewind symbol, thick dark outline, centered on a plain cream wall, no text.",
   "So let us rewind to the night you turned thirty-five.")

# ---- acto 2: el punto de partida ----
sc("WIDE", "KNIGHT", "a wide view of the kitchen at night, Sam small at the table with a single small cake and one lit candle in front of him, a dark window behind.",
   "Ten years earlier, it is your thirty-fifth birthday, and what keeps you awake is not the candles.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a closed laptop and a small piggy bank icon floating beside his head, a thoughtful look.",
   "You have a decent job, a small savings account, and no investments at all. Not one dollar.")
sc("HAND", "KNIGHT", "a hand scrolling a smartphone showing a feed of colorful gray blurred thumbnails, no readable text and no digits.",
   "Online, everyone seems to have started at twenty-two, with perfect spreadsheets and a calm voice.")
sc("CLOSE", "KNIGHT", "his face in close-up lit by the cold glow of a phone below the frame, a discouraged expression.",
   "You think it is too late. A voice in your head says the train has already left the station.")
sc("SIT", "OFFICE", "he sits at his cubicle looking down, a small coworker silhouette beside him gesturing cheerfully with a pen, a small green upward arrow floating near the coworker.",
   "At work, a colleague mentions that his retirement account is growing nicely, and you quietly change the subject.")
sc("HAND", "OFFICE", "a hand pressing the blank gray keys of a calculator on a desk, no readable text and no digits.",
   "That night you open a calculator, mostly to prove to yourself that it really is too late.")
sc("MACRO", "DESK", "a flat illustration of a calculator beside an hourglass with sand mostly in the bottom half, no text and no digits.",
   "You expect bad news, and you find some. Waiting does cost something, and pretending otherwise would be a lie.")
sc("SIT", "LIVING", "he sits on the couch with the calculator in his hands, a dawning surprise on his face, one lamp glowing.",
   "But then you notice a second thing. The calculator does not say zero. It says something.")
sc("CLOSE", "LIVING", "his face in close-up, eyes brightening slowly, warm lamp light on one cheek.",
   "The real question was never whether you could catch everyone. It was what you could build from here.")
sc("STAND", "KDAY", "he stands at the kitchen counter in morning light opening the gray notebook with the sprout on its cover, a pen in his hand.",
   "So you open a gray notebook and write one line on the first page. I start today.")
sc("HAND", "KDAY", "a hand writing in the gray notebook, the page filled with simple icons of a coin, a house and a plate, no letters and no digits.",
   "You list your income, your spending, and what you could invest each month without panic.")
sc("MACRO", "DESK", "a flat illustration of two coin stacks side by side, a tall one labeled by a small house icon and a shorter one beside a small shield icon, no text and no digits.",
   "In this example, you take home about five thousand dollars a month and decide to invest one thousand.")
sc("SIT", "KDAY", "he sits at the kitchen table with a mug, calm and resolute, a small crossed-out card icon floating next to him.",
   "That means trimming habits, not joy. A few subscriptions, a few delivery nights, and a car you keep longer.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a plain pale app with a flat green plant icon, no readable text and no digits.",
   "You open an account and pick a plain, low cost index fund, the kind that holds hundreds of companies.")
sc("STAND", "KDAY", "he stands at the counter tapping a smartphone, a small calendar icon with a loop arrow floating beside the screen.",
   "Then you automate the transfer, so the decision is made once, on a calm day, instead of every single month.")

# ---- acto 3: los años del medio ----
sc("SIT", "KDAY", "he sits at the table in morning light with a mug, a faint smile, a tiny sprout icon on the windowsill behind him.",
   "The first month feels exciting. The second feels normal. By the sixth, it feels almost boring.")
sc("MACRO", "DESK", "a flat illustration of a green line chart wobbling up and down while slowly trending upward, no text and no digits.",
   "In year one the line wobbles, and some months your balance is lower than what you put in.")
sc("CLOSE", "KNIGHT", "his face in close-up at night, brow slightly furrowed, a faint red glow on one cheek.",
   "That is when the old voice returns and whispers. Maybe this is not for people like you.")
sc("SIT", "LIVING", "he sits on the couch with the notebook on his knees and a steady expression, a small calendar icon floating beside his head.",
   "You remind yourself that you are not predicting next month. You are building for decades.")
sc("WIDE", "OFFICE", "a wide view of the office where a coworker silhouette leans toward Sam whispering with a hand beside his mouth, a sparkling star icon floating between them.",
   "A coworker leans over and whispers about a sure thing he heard from a friend of a friend.")
sc("CLOSE", "OFFICE", "his face in close-up, eyebrows slightly raised, tempted but thoughtful, soft office light.",
   "Your heart speeds up, because a sure thing would solve everything. Then you remember that sure things do not exist.")
sc("HAND", "OFFICE", "a hand holding up one finger in a polite no, a sparkling star icon fading in the blurred background.",
   "You politely say no, and you keep buying the same boring fund every single month.")
sc("STAND", "STREET", "he stands on the sidewalk with a small smile, a large glossy black SUV in the driveway behind him and the neighbor silhouette admiring it at the edge of the frame.",
   "At home your neighbor shows off his new black SUV, and you smile, because your money is busy somewhere quieter.")
sc("SIT", "LIVING", "he sits on the couch with a smartphone at his ear, a warm smile, the college friend silhouette shown as a small gray speech bubble icon beside his head.",
   "Your college friend calls. He started at twenty-five, and he is happy to share what he has learned.")
sc("CLOSE", "LIVING", "his face in close-up, nodding slowly while listening, warm lamp light.",
   "He says the best thing he did was not picking clever funds. It was never stopping.")
sc("HAND", "LIVING", "a hand resting on a phone placed on the couch arm, a soft glow from the screen, the other hand holding a mug.",
   "Then he admits something honest. His early start was luck as much as skill, because someone showed him how.")
sc("MACRO", "DESK", "a flat illustration of a small stack of coins with a green flag, a tiny arrow looping around it, no text and no digits.",
   "In year three you get a raise and send part to the fund. Our numbers do not even count it.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night reading a plain paper brochure drawn as gray lines, a small shield icon floating beside his head.",
   "You also ask about your employer plan, because some employers add matching money. It is worth one conversation.")
sc("MACRO", "DESK", "a flat illustration of a long green line starting low on the left and rising to a tall green flag on the right, a small sprout icon at the start, no text and no digits.",
   "Here is the honest math. Imagine someone who invests five hundred dollars a month starting at twenty-five.")
sc("HAND", "DESK", "a hand pointing a pen at a very tall coin stack with a small gold flag on top, drawn on a notebook page with a faint clock icon beside it, no text and no digits.",
   "At about six percent a year, that person would reach roughly one million dollars by the time they turn sixty-five.")
sc("MACRO", "DESK", "a flat illustration of a coin stack about half the height of the previous one with a flag on top, a clock icon behind it, no text and no digits.",
   "You, starting at thirty-five with the same five hundred dollars, would reach only about half a million.")
sc("CLOSE", "KNIGHT", "his face in close-up, quietly honest, jaw relaxed, a slight wince in the eyes.",
   "That gap hurts a little. Waiting ten years costs real money, and pretending it does not would not help you.")
sc("SIT", "KNIGHT", "he sits at the kitchen table with the notebook, a determined expression, a small up-arrow icon floating beside his head.",
   "But you can control something. You can invest more each month to close part of the gap.")
sc("MACRO", "DESK", "a flat illustration of two coin stacks of equal height with a double arrow between them and a small plus icon at the base of one, no text and no digits.",
   "Invest one thousand dollars a month from age thirty-five, and in this example you also reach about one million.")
sc("HAND", "KNIGHT", "a hand holding a pen over the notebook comparing two small coin stacks, one drawn tall and one drawn very tall, no letters and no digits.",
   "It is not free. You put in about three hundred sixty thousand dollars, versus two hundred forty thousand.")
sc("CLOSE", "LIVING", "his face in close-up, an honest, accepting expression, lamp light.",
   "So you catch up only by paying more each month. That is the honest price of starting late.")
sc("SIT", "LIVING", "he sits on the couch with open hands, a small icon of a cloud and a sun floating beside his head.",
   "This is an illustration. Markets may do better or worse, and nobody can promise you a single number.")
sc("WIDE", "STREET", "a modest house in the rain with a thin gray cloud above the roof and a small bucket icon beside the door, Sam small on the porch.",
   "In year six a roof leaks, and your budget is tested, but you cover it without touching the fund.")
sc("HAND", "KDAY", "a hand holding a small glass jar of coins with a flat shield icon on it, soft morning light.",
   "A small cash cushion made that possible, so your investments could keep doing their quiet work.")
sc("SIT", "KDAY", "he sits at the kitchen table with the gray notebook open, a pen in hand, a calm smile, sunlight on the page.",
   "Year after year the transfer goes out, and the account slowly grows. The notebook gets another line.")

# ---- acto 4: el giro / la prueba ----
sc("STAND", "KDAY", "he stands by the window in morning light holding the gray notebook open, a small green plant on the windowsill, a peaceful posture.",
   "Every January you open the notebook and add a line about what you learned.")
sc("WIDE", "LIVING", "a wide view of a family dinner table with several small silhouettes seated around it, Sam at one end holding a fork.",
   "At forty-two, someone at a family dinner asks the question you used to dread. Are you investing?")
sc("CLOSE", "LIVING", "his face in close-up, steady and sincere, warm dinner light on one cheek.",
   "You answer without shame. Yes, you say, I started late, and I started.")
sc("SIT", "LIVING", "he sits at the dinner table with a patient expression, two small cousin silhouettes leaning in beside him with curious faces.",
   "Nobody laughs. Two cousins quietly ask how they can begin, and one of them is only twenty-four.")
sc("HAND", "LIVING", "a hand sliding the gray notebook across the table toward the edge of the frame, a small sprout icon on its cover.",
   "You share your notebook, the simple steps, and the honest warning that nothing is guaranteed.")
sc("WIDE", "OFFICE", "a wide view of the office with Sam small at his cubicle and a younger coworker silhouette leaning on the partition, a calm green plant on the desk.",
   "At work, a coworker asks why money never seems to stress you. You say it is a habit, not a fortune.")
sc("HAND", "LIVING", "a hand holding a smartphone, the screen shows a pale line chart rising steadily, no readable text and no digits.",
   "So here you are again, forty-five, on the couch, with a balance of about one hundred sixty-four thousand dollars.")
sc("MACRO", "DESK", "a flat illustration of a medium coin stack with a small green flag on top, a clock icon behind it, no text and no digits.",
   "That is after ten years of investing one thousand dollars a month at about six percent.")
sc("CLOSE", "LIVING", "his face in close-up, a warm and honest smile, a faint reflection of a pale screen in his eyes.",
   "Your college friend shows about two hundred thirty thousand dollars. He is still ahead of you.")
sc("SIT", "LIVING", "he sits on the couch looking at the camera with a peaceful smile, the phone resting on his knee.",
   "But the gap between you is smaller than the gap between you and your old plan, which was nothing.")
sc("HAND", "LIVING", "a hand typing on a smartphone, a small heart icon floating above the screen, warm light.",
   "You type, congratulations, and you mean it. His start helped him, and your start is helping you.")
sc("STAND", "KDAY", "he stands at the counter writing a new line in the gray notebook with a pen, morning light, a small sprout icon floating above the page.",
   "Then you open the gray notebook and write a new line. Keep going, ten more years.")
sc("WIDE", "LIVING", "a wide view of the living room with Sam small on the couch, a faint dotted line drawn across the floor toward a tiny flag at the far wall.",
   "If you keep the habit for twenty more years, the illustration says the account could reach about one million dollars.")
sc("SIT", "LIVING", "he sits on the couch with a small smile, two fingers raised gently as if holding a delicate thing, a small cloud icon beside his head.",
   "Could, not will. You hold that word gently, and you keep walking anyway, one month at a time.")
sc("CLOSE", "KDAY", "his face in close-up, calm and certain, morning light across his eyes.",
   "The real mistake would not have been starting at thirty-five. It would have been waiting for thirty-six.")

# ---- cierre ----
sc("SIT", "KDAY", "he sits at the kitchen table looking at the camera with a warm, calm expression, a mug and the gray notebook in front of him.",
   "So here is your point of view. You are not behind. You are simply starting from exactly where you are today.")
sc("MACRO", "DESK", "an open notebook with a pen and a flat icon of a green plant beside a small coin stack, no letters and no digits.",
   "Step one, pick a simple, low cost, diversified fund, and decide the monthly amount you can keep up.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a plant, no readable text and no digits.",
   "Step two, automate the transfer for payday, and check whether your employer offers a match.")
sc("MACRO", "DESK", "a small calendar page drawn with empty squares and a green check icon beside a plain calculator with blank keys, no text and no digits.",
   "Step three, review once a year, raise the amount when you can, and ignore the noise in between.")
sc("STAND", "KDAY", "he stands at the kitchen counter in morning light, calm and steady, a small sprout icon floating over the window.",
   "A late start is expensive. But an even later start is more expensive, and every month still counts.")
sc("SIT", "CLEAN", "He sits at a table looking at the camera with a friendly smile; floating at the right next to his head, a large flat icon of a red subscribe button with a bell, thick outline, no text.",
   "If this story made you think about starting, subscribe, and come back for the next quiet story.")
sc("MACRO", "DESK", "a closed notebook with a pen on top and a hand-drawn shield icon on the cover, on a dark wooden table, no letters and no digits.",
   "This video is for education only, not financial advice. Rates, expenses and risks differ for everyone, so speak with a licensed professional about your own situation.")
sc("WIDE", "STREET", "he walks along a quiet street in the evening with the gray notebook under one arm, small and relaxed, a long warm sunset behind him.",
   "You walk through the evening with the old notebook under your arm and a calm, steady pace.")
sc("MACRO", "DESK", "the gray notebook with the tiny sprout on its cover on a dark wooden table beside a single coffee mug, soft morning light, no letters and no digits.",
   "The notebook is dusty. The start was late. The start counted.")

if __name__ == "__main__":
    emit(S, "v7", "Video 7: POV: You Started Investing at 35 - And Still Built Something Real")
