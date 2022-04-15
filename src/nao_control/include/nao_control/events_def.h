#ifndef ALL_EVENTS_DEF_H_
#define ALL_EVENTS_DEF_H_

#include <iostream>
#include "event.h"
#include <string>
#include "eventId.h"
#include <dispatchEventService.h>

using namespace std;


/**
 * @brief LeftLegEvent
 * 
 */

class LeftLegEvent : public CEvent{

public:
    LeftLegEvent();
    ~LeftLegEvent();
    string getPlaningGroup(){return this->planing_group;};
    bool move();

private:
    string planing_group = "LeftLeg";

};

/**
 * @brief RightLegEvent
 * 
 */

class RightLegEvent : public CEvent{

public:
    RightLegEvent();
    ~RightLegEvent();
    bool move();

private:
    string planing_group = "LeftLeg";
};

/**
 * @brief LeftHandEvent
 * 
 */

class LeftHandEvent : public CEvent
{

public:
    LeftHandEvent();
    ~LeftHandEvent();
    bool move();

private:
    string planing_group = "LeftHand";
};


/**
 * @brief RightHandEvent
 * 
 */

class RightHandEvent : public CEvent
{

public:
    RightHandEvent();
    ~RightHandEvent();
    bool move();

private:
    string planing_group = "RightHand";
};


#endif