"""
Net Worth POV - Video 4: "POV: You Retire 20 Years Before Everyone Else - Quietly"
Cifras ilustrativas: take-home 4000/mes, gasto 2000/mes = 24000/año; numero de libertad = 25 x 24000 = 600000; ahorro 24000/año a 5% real anual -> ~17 años (FV ~620000); amigo ahorra 10% (400/mes), gasta 43200/año -> numero 1080000, ahorra 4800/año -> mas de 50 años.
Uso: python netWorthPOV_v4_scenes.py
"""
from nwpov_common import emit

S = []
def sc(kind, setting, visual, narr):
    S.append((kind, setting, visual, narr))

# ---- gancho ----
sc("MACRO", "DESK", "a dented steel lunch box on a dark wooden table with a folded napkin and a fork beside it, a small hand-drawn sun icon on the lid, no letters and no digits.",
   "On an office desk sits a dented steel lunch box. It has made this trip almost daily for seventeen years.")
sc("SIT", "OFFICE", "He sits at his cubicle desk in a quiet office, hands folded, looking at the camera with a calm slight smile; a nearly empty desk around him.",
   "It is Friday afternoon, you are forty-five, and nobody around you knows this is your last day.")
sc("HAND", "OFFICE", "a hand sliding a small cardboard box across a desk, inside it a tiny green plant, a white mug and a framed photo drawn as a plain gray square.",
   "Your desk is almost empty. A plant, a mug, and one photo are all that remain.")
sc("WIDE", "OFFICE", "a wide view of the open office with rows of cubicles, three small gray silhouettes chatting near a water cooler far in the background, Sam tiny in the foreground.",
   "Your coworkers are talking about vacations, car payments, and how many years they still have left to work.")
sc("CLOSE", "OFFICE", "his face in close-up under soft office light, a calm, quietly confident expression, eyes looking slightly to the side.",
   "You do not say a word. You just smile, because you know something they do not.")
sc("HAND", "OFFICE", "a hand placing a plain access card on a closed laptop on the desk, no readable text and no digits.",
   "You set your access card on the closed laptop, and it makes the smallest sound in the world.")
sc("STAND", "STREET", "he walks out of glass office doors carrying the dented steel lunch box in one hand, bright afternoon light, a few small silhouettes of coworkers cropped at the edge.",
   "Most people your age are twenty years from retirement. You are walking out today.")
sc("MACRO", "CLEAN", "a large flat icon of two left-pointing arrows in a rewind symbol, thick dark outline, centered on a plain cream wall, no text.",
   "No lottery. No inheritance. No secret. So let us rewind to the day all of this began.")

# ---- acto 2: el punto de partida ----
sc("WIDE", "STREET", "he walks small along a quiet street toward a modest apartment building at dusk, a paper grocery bag in one arm, warm windows lit.",
   "Seventeen years earlier, you are twenty-eight, living in a rented apartment, earning a salary that is perfectly ordinary.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a closed laptop and a loose pile of bills drawn as gray blurred sheets, a single lamp glowing.",
   "About four thousand dollars arrives each month after taxes, and almost all of it disappears.")
sc("HAND", "KNIGHT", "a hand holding a smartphone tilted toward the camera, the screen shows a pale banking app with flat gray bars and one small red arrow, no readable text and no digits.",
   "You are not reckless. There is no luxury. The money simply leaks out through things you never really notice.")
sc("MACRO", "DESK", "on a dark wooden table, a takeout coffee cup, a crumpled receipt drawn as gray lines, and a small delivery bag, with tiny coin icons floating away from them.",
   "A coffee here, a delivered dinner there, a subscription you forgot about, and suddenly the month is gone.")
sc("SIT", "OFFICE", "he sits at his cubicle looking tired, a small silhouette of a coworker behind him holding up a car key fob, a large shiny pickup truck visible through the window.",
   "At work, the coworker in the next cubicle talks about his new truck like a trophy.")
sc("WIDE", "STREET", "an office parking lot in sunlight with one huge glossy pickup truck in the center, Sam tiny at the edge of the frame looking up at it.",
   "It is shiny, loud, and expensive, and for a moment you wonder whether you are the one falling behind.")
sc("CLOSE", "KNIGHT", "his face in close-up lit by the cold glow of a phone screen below the frame, a thoughtful and slightly worried expression.",
   "That night you look at your balance and feel a quiet worry. Where did all those paychecks actually go?")
sc("HAND", "KNIGHT", "a hand writing in an open spiral notebook with a pen, the page filled with small hand-drawn icons of a house, a bus, a plate and a coin, no letters and no digits.",
   "So you write down everything you spend for one month. It is uncomfortable, but it is honest.")
sc("MACRO", "DESK", "an open notebook page with colored horizontal bars: one very long bar, two medium bars, and a long tail of tiny bars, no readable text and no digits.",
   "Housing is the biggest piece. Food and transport come next. Then a long tail of small things you barely remember.")
sc("SIT", "LIVING", "he sits on the couch with the notebook open on his knees, chin resting on one hand, a floor lamp glowing beside him.",
   "You ask a simple question. If you lived on half of this, what would you actually miss?")
sc("CLOSE", "LIVING", "his face in close-up, eyebrows slowly rising as a small realization appears, warm lamp light on one cheek.",
   "The answer surprises you. Almost nothing important would disappear. Mostly it would be convenience, noise, and habit.")
sc("STAND", "KDAY", "he stands at the kitchen counter in morning light packing sandwiches and fruit into a plain new steel lunch box, a coffee mug beside him.",
   "So you buy a plain steel lunch box and pack your own lunch the next morning.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of a wallet with an arrow pointing to a small shield, no readable text and no digits.",
   "You also make one boring decision. Every payday, half of your take home pay moves automatically into investing.")
sc("MACRO", "DESK", "a flat illustration of two equal stacks of coins side by side, the left one with a small shield icon, the right one with a small house icon, no text.",
   "Two thousand dollars goes to the future. Two thousand is left for living. You never see the first half.")
sc("SIT", "KDAY", "he sits at the kitchen table sipping from a white mug, a calm slight smile, sunny window behind him.",
   "It feels strange for about three months, and then it feels normal. Habit quietly replaces willpower.")

# ---- acto 3: los años del medio ----
sc("WIDE", "STREET", "a suburban street at golden hour, a large glossy black SUV parked in a driveway on the right, Sam tiny on the sidewalk on the left.",
   "Years pass. Your neighbor pulls into his driveway with a glossy black SUV, and the street admires it.")
sc("STAND", "STREET", "he stands on the sidewalk with a friendly wave toward a cropped silhouette of the neighbor beside the large glossy black SUV at the edge of the frame.",
   "You wave, you smile, and tell him it looks great. You just do not want one.")
sc("CLOSE", "STREET", "his face in close-up, a gentle half smile, a blurred shiny black car reflecting a hint of sun behind him.",
   "Some people call you cheap. You prefer to think of it as choosing which things deserve your money.")
sc("SIT", "OFFICE", "he sits at his cubicle, a small green upward arrow floating near the monitor, the coworker silhouette with the truck keys passing by at the edge.",
   "Your salary slowly grows, but your spending stays put, so most of each raise becomes savings.")
sc("HAND", "LIVING", "a hand holding an older smartphone with a slightly scratched edge above a pair of comfortable worn sneakers, secondhand couch cushions at the bottom of the frame.",
   "Your phone is three years old. Your shoes are comfortable. Your couch came secondhand, and it works perfectly well.")
sc("MACRO", "DESK", "a flat illustration of a green line chart gently rising with bumps, small coin stacks growing along its base, no text and no digits.",
   "Every month the same two thousand dollars goes into a plain, low cost index fund holding many companies.")
sc("SIT", "LIVING", "he sits on the couch with a calm face, a simple wall calendar page with blank squares behind him, evening light.",
   "Nothing exciting happens. Some months the balance rises. Some months it falls. You keep adding the same amount anyway.")
sc("STAND", "OFFICE", "he stands at his desk opening the dented steel lunch box, three coworker silhouettes cropped at the edge holding takeout bags and laughing.",
   "At lunch everyone orders out. You open your dented lunch box, and someone jokes about a yacht.")
sc("CLOSE", "OFFICE", "his face in close-up, laughing softly with warm eyes, a faint blur of coworkers behind him.",
   "You laugh along. You are not saving for a yacht. You are saving for mornings with nowhere to be.")
sc("WIDE", "STREET", "he stands very small on a grassy hill at sunset looking toward a faint horizon line, a long quiet path behind him.",
   "To you, freedom is not a place or a thing. It is the ability to say no.")
sc("MACRO", "DESK", "a flat illustration of a simple calculator with blank gray keys and a pencil next to a notebook, no readable text and no digits.",
   "One evening you learn a rule of thumb. Multiply a year of spending by twenty-five to get your freedom number.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with the notebook open and a pencil in his hand, a thoughtful look, one lamp glowing.",
   "You spend about twenty-four thousand dollars a year, so your freedom number is roughly six hundred thousand dollars.")
sc("HAND", "KNIGHT", "a hand drawing a big arrow up a staircase in a notebook margin, small stacked coins drawn on each step, no letters and no digits.",
   "That sounds huge, until you notice you add twenty-four thousand every year, and the money starts working too.")
sc("MACRO", "DESK", "a flat illustration of a small green plant growing from a stack of coins, with a faint clock icon behind it, no text.",
   "If investments grow about five percent a year after inflation, you would reach that number in roughly seventeen years.")
sc("CLOSE", "LIVING", "his face in close-up, eyes narrowed in a thoughtful way, soft lamp light.",
   "Compare that with a friend who saves ten percent and spends the rest. Same salary, very different timeline.")
sc("MACRO", "CLEAN", "two simple paths drawn on a cream wall: a short steep green line climbing to a small flag, and a very long winding gray line that fades into the distance, no text.",
   "He spends more, so his number is higher. In this example, that takes more than fifty years.")
sc("SIT", "KDAY", "he sits at the kitchen table holding a mug, looking at the camera with a calm expression, morning light.",
   "Nothing about this is magic. It is a gap between earning and spending, held steady for years.")
sc("WIDE", "OFFICE", "a quiet open office where all the silhouettes of coworkers stand frozen around a manager at the front, Sam tiny at his cubicle.",
   "In year nine, your company announces layoffs. The office goes silent, and people stare at their screens.")
sc("CLOSE", "OFFICE", "a cropped silhouette of the coworker with the truck keys at the edge of the frame, his shoulders slumped, with Sam's calm face in the foreground.",
   "The coworker with the new truck goes pale. He has a loan, a lease, and almost nothing set aside.")
sc("SIT", "LIVING", "he sits on the couch with a laptop open on his knees, the screen turned away, a slow exhale, a small shield icon floating near his head.",
   "That night you check your accounts. You have a cushion, investments, and a life that costs very little.")
sc("HAND", "LIVING", "a hand holding a coffee mug with a small white shield icon drawn on it, the other hand resting on the couch arm.",
   "You keep your job, but the scare changes something. You see how much calm your boring plan buys.")
sc("WIDE", "STREET", "a gray cloudy city skyline with a big red downward arrow icon in the sky, Sam tiny in the foreground on a sidewalk.",
   "Around then the market falls. Your balance drops for months, and it hurts to look at.")
sc("CLOSE", "KNIGHT", "his face in close-up at night, jaw tight, one hand hovering over a phone just out of frame, a faint red glow on his cheek.",
   "You want to sell. Instead you wait, keep contributing, and remind yourself this was part of the deal.")
sc("MACRO", "DESK", "a flat illustration of a green line chart dipping low and then climbing back above its old peak, a small flag at the top, no text and no digits.",
   "Slowly the line climbs again. Because you kept buying while prices were low, recovery comes sooner.")
sc("SIT", "KDAY", "he sits at the kitchen table with the dented steel lunch box open in front of him, a half-eaten sandwich, a calm smile.",
   "Year after year you repeat the routine. The lunch box gets another dent, and your balance gets another layer.")

# ---- acto 4: el giro / la prueba ----
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a pale line chart rising to a small green flag, no readable text and no digits.",
   "In your forty-fifth year, you open your account, and the balance finally passes six hundred thousand dollars.")
sc("CLOSE", "KDAY", "his face in close-up, calm and a little stunned, soft morning light, a very small smile.",
   "You expected fireworks. Instead you feel quiet and careful, like someone at the top of a long staircase.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a notebook and a shield icon floating beside his head, reading carefully with a pencil in hand.",
   "You do not quit that night. You check your spending, your insurance, and your plan, line by line, twice.")
sc("MACRO", "DESK", "a flat illustration of a small stack of coins with a thin arrow flowing out to a tiny house icon, no text and no digits.",
   "Four percent of six hundred thousand dollars is twenty-four thousand a year. That matches the life you already live.")
sc("HAND", "KNIGHT", "a hand holding a pencil circling a small umbrella icon drawn in a notebook, beside a heart icon and a coin icon, no letters and no digits.",
   "This is a simplified rule. Taxes, health costs, and market swings are real, so you keep an extra cushion.")
sc("STAND", "OFFICE", "he stands in front of a manager silhouette at a desk, handing over a plain white envelope, a calm and polite posture.",
   "You tell your manager you are leaving. He asks which job you got, and you say none.")
sc("CLOSE", "OFFICE", "a cropped silhouette of the manager at the edge of the frame with Sam's calm face in the foreground, a warm window light behind.",
   "He laughs, then stops. Then he asks, very quietly, how long you have been planning this.")
sc("SIT", "OFFICE", "he sits across a small desk from the manager silhouette, hands open, a gentle shrug, a small clock icon floating near his head.",
   "You tell him it was never a grand plan. It was a small decision, repeated for seventeen years.")
sc("WIDE", "STREET", "a suburban driveway in the evening, the black SUV parked large in the foreground, the neighbor silhouette standing beside it, Sam tiny on the sidewalk.",
   "The neighbor with the black SUV hears the news and shakes his head. He still owes on that car.")
sc("STAND", "STREET", "he stands on the sidewalk gesturing with open palms toward the neighbor silhouette cropped at the edge, a relaxed posture.",
   "He asks how. You tell him you did not earn more. You simply spent less than you earned.")
sc("CLOSE", "STREET", "his face in close-up, gentle and a little sympathetic, the blurred black SUV behind him at dusk.",
   "He nods slowly, like someone doing a hard sum in his head, and he looks tired.")
sc("HAND", "OFFICE", "a hand holding a plastic fork above a small slice of cake on a paper plate, a signed card drawn as a plain folded rectangle beside it, no readable text.",
   "On your last Friday, the team signs a card and brings a cake. Everyone says you are lucky.")
sc("CLOSE", "OFFICE", "his face in close-up with a warm honest smile, eyes soft, blurred party colors behind him.",
   "You smile, because luck helped. Good health, steady work, and decent markets mattered. So did seventeen years of choices.")
sc("MACRO", "DESK", "a flat illustration of an open umbrella over a small house icon with raindrops falling around it, no text.",
   "Luck decides the weather. Habits decide whether you have a roof when it rains.")
sc("STAND", "OFFICE", "he lifts the dented steel lunch box from his empty desk in warm late light, the cardboard box with the plant under his other arm.",
   "And so we come back to that last afternoon, and the lunch box in your hand.")

# ---- cierre ----
sc("SIT", "KDAY", "he sits at the kitchen table looking at the camera with a warm, calm expression, a mug and a notebook in front of him.",
   "So here is your point of view. You do not need a huge salary. You need a gap and a direction.")
sc("MACRO", "DESK", "a notebook open with a pen resting on it, a flat icon of a magnifying glass over a coin on the page, no text and no digits.",
   "Step one, track your spending for one month without judgment, so you can see where your money truly goes.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a shield, no readable text and no digits.",
   "Step two, automate a fixed share of every paycheck into a low cost, diversified fund.")
sc("MACRO", "DESK", "a calculator with blank gray keys beside a small calendar page drawn with empty squares and a green check icon, no text and no digits.",
   "Step three, work out your own freedom number, and check it once a year, because your life will change.")
sc("STAND", "KDAY", "he stands in the kitchen in morning light closing the dented steel lunch box with a satisfied look, a small sun icon floating over the window.",
   "Fast or slow, any gap between earning and spending is a form of freedom. Even a small one counts.")
sc("SIT", "CLEAN", "He sits at a table looking at the camera with a friendly smile; floating at the right next to his head, a large flat icon of a red subscribe button with a bell, thick outline, no text.",
   "If this story made you think about your own gap, subscribe, and come back for the next quiet story.")
sc("MACRO", "DESK", "a closed notebook with a pen on top and a hand-drawn shield icon on the cover, on a dark wooden table, no letters and no digits.",
   "This video is for education only, not financial advice. Rates, expenses and risks differ for everyone, so speak with a licensed professional about your own situation.")
sc("WIDE", "STREET", "he walks away down a long sunny sidewalk with the dented steel lunch box swinging from one hand, small and relaxed, a wide open sky above him.",
   "You step outside, and the air feels lighter, like a calendar that belongs to you again.")
sc("MACRO", "DESK", "the dented steel lunch box on a dark wooden table beside a single coffee mug in soft morning light, no letters and no digits.",
   "The lunch box is dented. You are free.")

if __name__ == "__main__":
    emit(S, "v4", "Video 4: POV: You Retire 20 Years Before Everyone Else - Quietly")
