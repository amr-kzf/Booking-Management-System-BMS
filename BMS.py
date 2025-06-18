from rich.console import Console
console = Console()

# بيانات الحجوزات للخدمة الأولى
new_car_id = [
    ["13-04-2025", "Sunday", [6, 10, 1, 10, 7]],
    ["14-04-2025", "Monday", [10, 2, 10, 6, 4]],
    ["15-04-2025", "Tuesday", [3, 1, 10, 10, 9]],
    ["16-04-2025", "Wednesday", [10, 8, 10, 7, 3]],
    ["17-04-2025", "Thursday", [2, 10, 4, 10, 1]]
]

# حساب المتوسط
def calculate_mean(service_data):
    total_reservations = sum([sum(day[2]) for day in service_data])
    total_slots = len(service_data) * len(service_data[0][2])
    mean = total_reservations / total_slots
    return mean

mean_service1 = calculate_mean(new_car_id)
print(f"Mean of reservations for Service#1: {mean_service1:.2f}")

# إيجاد اليوم الأكثر ازدحامًا
def most_crowded_day(service_data):
    totals = [sum(day[2]) for day in service_data]
    max_total = max(totals)
    max_index = totals.index(max_total)
    return service_data[max_index][1], max_total

# إيجاد اليوم الأقل ازدحامًا
def least_crowded_day(service_data):
    totals = [sum(day[2]) for day in service_data]
    min_total = min(totals)
    min_index = totals.index(min_total)
    return service_data[min_index][1], min_total

most_crowded, max_reservations = most_crowded_day(new_car_id)
least_crowded, min_reservations = least_crowded_day(new_car_id)

print(f"Most Crowded Day for Service#1: {most_crowded} with {max_reservations} reservations")
print(f"Least Crowded Day for Service#1: {least_crowded} with {min_reservations} reservations")

# التحقق من قوة كلمة المرور
def is_strong_password(password):
    if len(password) != 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not password.isalpha(): 
        return False
    return True

# تسجيل المستخدم
def register_user():
    console.print("🎉 Welcome to the Booking Management System! 🎉", style="bold green")
    username = input("👤 Enter your username: ")
    while True:
        password = input("🔒 Enter a strong password (8 characters, mix of upper and lower case, no numbers or special characters): ")
        if is_strong_password(password):
            confirm_password = input("🔑 Confirm your password: ")
            if password == confirm_password:
                console.print("✅ Successful Registration! 🎉", style="bold green")
                return username, password
            else:
                console.print("❌ Passwords mismatched, please try again.", style="bold red")
        else:
            console.print("⚠️ Weak password, please try again.", style="bold yellow")

# تسجيل الدخول
def login_user(registered_username, registered_password):
    console.print("🔐 Please log in", style="bold blue")
    while True:
        username = input("👤 Enter your username: ")
        password = input("🔒 Enter your password: ")
        if username == registered_username and password == registered_password:
            console.print(f"🎉 Welcome {username}! 🎉", style="bold green")
            return True
        else:
            console.print("❌ Incorrect username or password. Please try again.", style="bold red")

# عرض الخدمات
services = [
    "New Car ID",
    "Renew Car ID",
    "New Driving License",
    "Renew Driving License",
    "Lost ID"
]

def display_services():
    console.print("📋 Available Services:", style="bold blue")
    for i, service in enumerate(services, 1):
        console.print(f"{i}. {service} 🚗")

# عرض الأيام
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

def display_days():
    console.print("📅 Available Days:")
    for i, day in enumerate(days, 1):
        console.print(f"{i}. {day} 🌞")

# اختيار الخدمة واليوم والوقت
def book_service():
    display_services()
    service_choice = int(input("👉 Please select a service (1-5): "))
    selected_service = services[service_choice - 1]

    display_days()
    day_choice = int(input("👉 Please select a day (1-5): "))
    selected_day = days[day_choice - 1]

    # عرض الأوقات المتاحة
    selected_day_data = new_car_id[day_choice - 1]
    available_slots = selected_day_data[2]
    console.print("⏰ Available Slots:")
    for i, slot in enumerate(available_slots, 1):
        console.print(f"{i}. {9 + i}:00AM - Remaining: {10 - slot} bookings")

    while True:
        slot_choice = int(input("👉 Please select a slot (1-5): "))
        if available_slots[slot_choice - 1] < 10:  # تحقق من أن هناك أماكن متاحة
            selected_slot = f"{9 + slot_choice}:00AM"
            break
        else:
            console.print("❌ This slot is fully booked. Please select another slot.")

    # إدخال بيانات المستخدم
    full_name = input("📝 Enter your full name: ")
    id_number = input("🆔 Enter your ID number: ")

    # تأكيد الحجز
    console.print("\n🎉 Reservation Confirmed! 🎉")
    console.print(f"👤 Name: {full_name}")
    console.print(f"🆔 ID: {id_number}")
    console.print(f"🛠️ Service: {selected_service}")
    console.print(f"📅 Day: {selected_day}")
    console.print(f"⏰ Slot: {selected_slot}")

def collect_feedback():
    while True:
        try:
            console.print("⭐ Please rate our service (1-5): ")
            rating = int(input("Your rating: "))
            if 1 <= rating <= 5:
                console.print("✅ Thank you for your feedback! 😊")
                break
            else:
                console.print("❌ Invalid rating. Please enter a number between 1 and 5.")
        except ValueError:
            console.print("⚠️ Invalid input. Please enter a valid number between 1 and 5.")

def cancel_booking():
    console.print("❌ Cancel Booking")
    confirmation = input("Are you sure you want to cancel your booking? (yes/no): ")
    if confirmation.lower() == "yes":
        console.print("Your booking has been canceled.")
    else:
        console.print("Cancellation aborted.")

def show_statistics(service_data):
    total_reservations = sum([sum(day[2]) for day in service_data])
    console.print(f"📊 Total Reservations: {total_reservations}")

# النظام الرئيسي
def main():
    console.print("🚗 Welcome to the Car Licensing Booking System! 🚗", style="bold cyan")
    
    # متغيرات لتخزين بيانات المستخدم المسجل
    registered_username = None
    registered_password = None

    while True:
        console.print("👉 Please choose an option:", style="bold blue")
        console.print("1. Sign Up", style="bold green")
        console.print("2. Log In", style="bold yellow")
        choice = input("Your choice (1/2): ")
        
        if choice == "1":
            # تسجيل المستخدم
            username, password = register_user()
            registered_username = username
            registered_password = password
            console.print("✅ You can now log in with your credentials.", style="bold green")
        
        elif choice == "2":
            # التحقق من وجود بيانات تسجيل
            if registered_username is None or registered_password is None:
                console.print("⚠️ No registered users found. Please Sign Up first.", style="bold yellow")
                continue
            
            # تسجيل الدخول
            if login_user(registered_username, registered_password):
                book_service()
                collect_feedback()
                show_statistics(new_car_id)
                cancel_booking()
                break
        
        else:
            console.print("❌ Invalid choice. Please select 1 or 2.", style="bold red")

# تشغيل النظام
main()