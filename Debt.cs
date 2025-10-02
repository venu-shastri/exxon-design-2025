using System;

class Icon
{
    float speed, glow, energy;
    int x, y;
    int subtype; // spinner, slider or hopper

    bool clockwise; // need for spinner
    bool expand;    // need for spinner
    bool vertical;  // need for slider

    int distance;   // need for slider
    bool visible;   // need for hopper

    int xcoord, ycoord; // need for hopper

    void Spin() { }

    void Slide() { }

    void Hop() { }

    // constructor must set subtype: client must pass value
    public Icon(uint value)
    {
        subtype = (int)value; // use enum for readability
        // and then use conditional to set associated fields
    }

    public void Move()
    {
        if (subtype == 1)
        {
            Spin();
        }
        else if (subtype == 2)
        {
            Slide();
        }
        else
        {
            Hop();
        }
    }

    // tedious subtype checking: subtype drives flair details
    public void Flair()
    {
        if (subtype == 1)
        {
            Spin();
        }
        else if (subtype == 2)
        {
            Slide();
        }
        else
        {
            Hop();
        }
    }
}
