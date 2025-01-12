// just emagine !! .. . . . .

#include <iostream>
#include <string>

using namespace std;

class basic_character {
    protected:
    int hp;
    int attack_damage;
    int stamina;

    public:
    basic_character() {
        hp = 100;
        attack_damage = 20;
        stamina = 50;
    }

    void set_hp(int x) {
        hp = x;
    }

    void set_attack_damage(int y) {
        attack_damage = y;
    }

    void set_stamina(int z) {
        stamina = z;
    }

    virtual ~basic_character() { }
};

class main_character : public basic_character {
    public:
    int attack_pistol() {
        cout << "-100" << endl;
        return attack_damage;
    }

    int attack_shotgun() {
        cout << "-1000" << endl;
        return attack_damage * 10;
    }

    int attack_rifle() {
        cout << "-200" << endl;
        return attack_damage * 2;
    }

    void put_armer(int h) {
        hp += h;
    }

    ~main_character() {
        cout << "YOU DIED" << endl;
    }
};

class monster : public basic_character {
    public:
    int attack() {
        cout << "-100" << endl;
        return attack_damage;
    }

    int special_attack() {
        for (int i = 0; i < 3; i++) {
            cout << "-100" << endl;
        }
        return attack_damage * 3;
    }

    ~monster() {
        cout << ":P" << endl;
    }
};

class combine : public basic_character {
    public:
    int attack_with_weapon() {
        cout << "-300" << endl;
        return attack_damage * 3;
    }

    int special_attack_RPG() {
        cout << "-3000" << endl;
        return attack_damage * 30;
    }

    ~combine() {
        cout << " !!" << endl;
    }
};

int main() {
    main_character* golden_freeman = new main_character();
    monster* headcrab = new monster();
    combine* geil = new combine();

    golden_freeman->set_hp(5000);
    golden_freeman->set_stamina(100);
    golden_freeman->set_attack_damage(100);

    headcrab->set_hp(500);
    headcrab->set_stamina(50);
    headcrab->set_attack_damage(100);

    geil->set_hp(3000);
    geil->set_stamina(100);
    geil->set_attack_damage(100);



    delete golden_freeman;
    delete headcrab;
    delete geil;

    return 0;
}