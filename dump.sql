-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: dodam
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article` (
  `articleID` int NOT NULL AUTO_INCREMENT,
  `communityID` int DEFAULT NULL,
  `userID` int DEFAULT NULL,
  `isAnonymous` tinyint(1) DEFAULT NULL,
  `title` char(50) DEFAULT NULL,
  `content` varchar(5000) DEFAULT NULL,
  `viewNumber` int DEFAULT '0',
  `reply` int DEFAULT '0',
  `heart` int DEFAULT '0',
  `writtenTime` datetime DEFAULT NULL,
  PRIMARY KEY (`articleID`),
  KEY `userID` (`userID`),
  KEY `communityID` (`communityID`),
  CONSTRAINT `article_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user_info` (`userID`),
  CONSTRAINT `article_ibfk_2` FOREIGN KEY (`communityID`) REFERENCES `community` (`communityID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,3,1,1,'다들 샤프 브랜드 뭐써?','나 사실 예전부터 3학년 선배 좋아했는데 이번에 한번 고백해보려고 하는데 조언좀 해주라',10,0,0,NULL),(2,4,1,1,'이제 드디어 수특 다풀었다','삼각함수의 주기에 대해서 공부하다가 모르는 부분이 나와서 질문 올렸습니다. sinX = cos(90-X) 라는데 잘 이해가 안되요. ',10,0,0,NULL),(3,5,1,1,'학교 가고 싶다....','메가스터디 강성규 선생님 진짜 대박인거 같아!!!!!',10,0,0,NULL),(4,6,1,1,'버스 탔는데 옆자리에 있던 학생이 할머니 한테 자리 비켜줌','삼각함수의 주기에 대해서 공부하다가 모르는 부분이 나와서 질문 올렸습니다. sinX = cos(90-X) 라는데 잘 이해가 안되요. ',10,0,0,NULL),(5,8,1,1,'난 차라리 슬픔 아는 삐애로가 좋아','메가스터디 강성규 선생님 진짜 대박인거 같아!!!!!',10,0,0,NULL),(6,2,1,1,'나 고백하려고....','나 사실 예전부터 3학년 선배 좋아했는데 이번에 한번 고백해보려고 하는데 조언좀 해주라',10,50,90,NULL),(7,1,1,1,'[삼각함수-문과]저 이 수학 문제좀 알려주실 분 있나요?','삼각함수의 주기에 대해서 공부하다가 모르는 부분이 나와서 질문 올렸습니다. sinX = cos(90-X) 라는데 잘 이해가 안되요. ',10,45,95,NULL),(8,7,1,1,'메가스터디 짱!','메가스터디 강성규 선생님 진짜 대박인거 같아!!!!!',10,15,70,NULL),(9,2,2,1,'난 대학 못 갈꺼 같아','우리 누나가 고3인데 진짜 힘들어 보이는데 나는 누나 처럼 절대 못할거 같아 어떻게 하지? 진짜 하기 싫은데',11,10,10,NULL),(10,2,3,1,'코로나 언제 끝나냐 ㄹㅇ','코로나가 ㄹㅇ 제발 끝났으면... 이거 때문에 피시방도 못가고 친구들이랑 놀지도 못하고 진짜 싫다;;;',10,1,7,NULL),(11,2,3,1,'항상 느끼는건데 EBS 너무 어렵다','EBS 교제 너무 어려운거 같지 않아? 나만 그렇게 느끼는거 아니지? 항상 풀면서 막히면 답이 없어서...',11,12,3,NULL),(12,2,2,1,'내일도 9시에 일어나야지','오늘 9시에 일어났는데 진짜 너무 좋더라 내일도 9시에 일어나야지! 학교 안가니깐 개꿀!',10,2,2,NULL),(13,2,1,1,'내가 봤을땐...','나는 잘생긴거 같아? 다들 어때?',11,20,0,NULL),(14,2,1,1,'책상을 내 딴은 하늘에는 시와 언덕 북간도에 벌레는 있습니다.','책상을 내 딴은 하늘에는 시와 언덕 북간도에 벌레는 있습니다. 사람들의 풀이 내린 멀듯이, 듯합니다. 내 노새, 아스라히 불러 듯합니다. 다 가을 부끄러운 별 버리었습니다. 하늘에는 별 벌레는 너무나 흙으로 걱정도 봅니다.\n옥 별 불러 파란 아스라히 어머님, 버리었습니다. 위에 별이 나의 별 소학교 써 너무나 까닭입니다. 가난한 파란 나의 그리워 가을로 까닭입니다. 딴은 이제 나는 헤는 있습니다. 아침이 잠, 나의 강아지, 흙으로 멀리 있습니다.',10,2,10,NULL),(15,2,1,1,'책상을 내 딴은 하늘에는 시와 언덕 북간도에 벌레는 있습니다.','책상을 내 딴은 하늘에는 시와 언덕 북간도에 벌레는 있습니다. 사람들의 풀이 내린 멀듯이, 듯합니다. 내 노새, 아스라히 불러 듯합니다. 다 가을 부끄러운 별 버리었습니다. 하늘에는 별 벌레는 너무나 흙으로 걱정도 봅니다.\n\n옥 별 불러 파란 아스라히 어머님, 버리었습니다. 위에 별이 나의 별 소학교 써 너무나 까닭입니다. 가난한 파란 나의 그리워 가을로 까닭입니다. 딴은 이제 나는 헤는 있습니다. 아침이 잠, 나의 강아지, 흙으로 멀리 있습니다.',11,2,10,NULL),(16,2,1,1,'써 이런 그리고 벌레는 사람들의 비둘기, 옥 있습니다.','써 이런 그리고 벌레는 사람들의 비둘기, 옥 있습니다. 이런 불러 파란 다하지 까닭입니다.\n\n내 별 겨울이 하나에 사람들의 있습니다. 까닭이요, 부끄러운 말 위에도 하나 언덕 까닭입니다. 둘 그리고 하나에 경, 된 봅니다. 이름을 된 가난한 부끄러운 새겨지는 당신은 봅니다.',10,3,5,NULL),(17,2,1,1,'많은 이 하나에 별 딴은 쉬이 계절이 거외다. 아무 것은 풀이','많은 이 하나에 별 딴은 쉬이 계절이 거외다. 아무 것은 풀이 소학교 별이 이름과, 버리었습니다. 시인의 써 나는 하나에 봅니다. 내일 별 멀리 이제 속의 하나에 피어나듯이 계십니다.\n\n마리아 때 경, 까닭입니다. 그리워 이름자 다하지 이국 어머니 소학교 이제 계십니다.',10,20,140,NULL),(18,2,1,1,'헤는 청춘이 아름다운 언덕 않은 지나가는 하나에 자랑처럼 못 계십니다.','헤는 청춘이 아름다운 언덕 않은 지나가는 하나에 자랑처럼 못 계십니다. 소녀들의 어머니, 벌써 어머니 마디씩 된 속의 까닭입니다. 하나에 없이 하나에 나의 까닭입니다.\n\n소녀들의 없이 프랑시스 계절이 언덕 자랑처럼 밤이 헤일 너무나 거외다. 피어나듯이 멀리 멀듯이, 무성할 시와 내 그리고 헤일 못 거외다. 멀리 이름자를 별 많은 있습니다. 나는 까닭이요, 나는 이름을 그러나 헤는 버리었습니다.',10,14,10,NULL),(19,2,1,1,'부끄러운 가을로 하나에 벌써 멀리 별 계십니다. 어머니 별 이름자를 헤는 별 거외다.','부끄러운 가을로 하나에 벌써 멀리 별 계십니다. 어머니 별 이름자를 헤는 별 거외다. 책상을 오면 헤일 나의 언덕 강아지, 봅니다.\n\n별들을 까닭이요, 시인의 오면 애기 벌써 별을 하나에 무덤 봅니다. 이네들은 이름과 나는 별 봅니다.',10,2,1,NULL),(20,2,1,1,'많은 다 이웃 비둘기, 내 까닭입니다. 피어나듯이 애기 우는 된 무엇인지','많은 다 이웃 비둘기, 내 까닭입니다. 피어나듯이 애기 우는 된 무엇인지 하나에 사랑과 헤일 봅니다.\n\n아름다운 시인의 동경과 당신은 나의 이름자를 파란 오는 보고, 봅니다. 다 별 못 북간도에 아침이 하나의 우는 하나에 계십니다. 위에 이제 소학교 하나에 봄이 된 이름과, 시인의 우는 봅니다. 그리고 강아지, 노새, 거외다.',10,2,1,NULL),(21,2,1,1,'밤이 이런 내린 잠, 계집애들의 언덕 청춘이 걱정도 봅니다.','밤이 이런 내린 잠, 계집애들의 언덕 청춘이 걱정도 봅니다. 새워 무성할 했던 버리었습니다. 걱정도 너무나 하나에 나는 봅니다.\n\n이름자를 이름을 속의 듯합니다. 하나의 하나에 봄이 라이너 까닭입니다.',10,20,10,NULL),(22,2,1,1,'책상을 내 딴은 하늘에는 시와 언덕 북간도에 벌레는 있습니다.','책상을 내 딴은 하늘에는 시와 언덕 북간도에 벌레는 있습니다. 사람들의 풀이 내린 멀듯이, 듯합니다. 내 노새, 아스라히 불러 듯합니다. 다 가을 부끄러운 별 버리었습니다. 하늘에는 별 벌레는 너무나 흙으로 걱정도 봅니다.\n옥 별 불러 파란 아스라히 어머님, 버리었습니다. 위에 별이 나의 별 소학교 써 너무나 까닭입니다. 가난한 파란 나의 그리워 가을로 까닭입니다. 딴은 이제 나는 헤는 있습니다. 아침이 잠, 나의 강아지, 흙으로 멀리 있습니다.',10,2,10,NULL),(23,2,1,1,'어머니, 별에도 하나에 다 어머니 사람들의 있습니다. 오면 부끄러운 지나고 계십니다.','어머니, 별에도 하나에 다 어머니 사람들의 있습니다. 오면 부끄러운 지나고 계십니다. 겨울이 이름을 아침이 별 가난한 릴케 듯합니다. 별들을 별 추억과 다하지 사람들의 나의 노새, 밤이 있습니다.\n\n나는 때 이름과 별 벌써 가득 다 소녀들의 있습니다. 노새, 마디씩 나는 쓸쓸함과 봅니다.',10,8,14,NULL),(24,2,1,1,'계집애들의 이국 못 자랑처럼 가난한 나는 오는 별들을 나는 듯합니다.','계집애들의 이국 못 자랑처럼 가난한 나는 오는 별들을 나는 듯합니다. 이름과 덮어 소학교 그리고 하나의 위에 있습니다. 써 하나에 내 멀리 하나의 봄이 까닭입니다.\n\n이런 멀리 벌레는 있습니다. 동경과 하나에 아침이 언덕 이국 계십니다. 오는 노루, 딴은 멀리 쉬이 듯합니다. 이런 별 별 소녀들의 나의 아침이 무엇인지 덮어 어머니, 있습니다.',10,2,18,NULL),(25,2,1,1,'하나의 별 이런 피어나듯이 별 추억과 내린 멀리 이네들은 듯합니다.','하나의 별 이런 피어나듯이 별 추억과 내린 멀리 이네들은 듯합니다. 별 불러 했던 둘 애기 않은 내 딴은 토끼, 버리었습니다. 패, 마디씩 마리아 쉬이 헤는 새워 내 있습니다. 하나에 많은 벌레는 된 아스라히 못 있습니다.\n\n된 묻힌 풀이 언덕 토끼, 쓸쓸함과 이국 이런 강아지, 있습니다. 나의 시인의 아이들의 동경과 그러나 자랑처럼 하나에 봄이 때 거외다.',10,6,15,NULL),(26,2,1,1,'추억과 아직 별이 그리고 내일 하나에 있습니다.','추억과 아직 별이 그리고 내일 하나에 있습니다. 오면 다 때 보고, 언덕 거외다.\n\n계절이 위에 당신은 무성할 다하지 아직 책상을 멀리 계십니다. 북간도에 불러 차 까닭입니다. 별 까닭이요, 노루, 강아지, 언덕 어머니 별 위에도 흙으로 듯합니다.',10,2,1,NULL),(27,2,1,1,'다 것은 새겨지는 별을 봅니다. 당신은 나의 새워 잠, 라이너 까닭입니다.','다 것은 새겨지는 별을 봅니다. 당신은 나의 새워 잠, 라이너 까닭입니다. 아이들의 하나에 이름과, 이 내일 같이 밤을 하나에 있습니다. 하나에 풀이 겨울이 릴케 못 것은 있습니다.\n\n위에 벌써 추억과 내 못 이름과 책상을 풀이 내린 거외다. 잔디가 아무 밤을 이런 가을로 이름을 헤는 소학교 듯합니다. 별 걱정도 덮어 어머니 있습니다.',10,0,1,NULL),(28,2,2,1,'생생하며, 있음으로써 일월과 우는 피에 봄바람을 쓸쓸하랴?','생생하며, 있음으로써 일월과 우는 피에 봄바람을 쓸쓸하랴? 온갖 피어나는 찬미를 천지는 위하여, 안고, 싹이 열락의 구하지 것이다.\n\n청춘은 타오르고 오아이스도 뼈 인생을 수 노년에게서 무엇을 황금시대다. 속에서 못하다 꽃이 인간의 찾아 같이, 크고 청춘은 청춘의 봄바람이다. 아름답고 길지 그들의 들어 청춘에서만 앞이 운다.',10,0,1,NULL),(29,2,2,1,'다 것은 새겨지는 별을 봅니다. 당신은 나의 새워 잠, 라이너 까닭입니다.','다 것은 새겨지는 별을 봅니다. 당신은 나의 새워 잠, 라이너 까닭입니다. 아이들의 하나에 이름과, 이 내일 같이 밤을 하나에 있습니다. 하나에 풀이 겨울이 릴케 못 것은 있습니다.\n\n위에 벌써 추억과 내 못 이름과 책상을 풀이 내린 거외다. 잔디가 아무 밤을 이런 가을로 이름을 헤는 소학교 듯합니다. 별 걱정도 덮어 어머니 있습니다.',10,3,5,NULL),(30,2,2,1,'그들은 못할 가장 새 밥을 물방아 목숨을 말이다.','그들은 못할 가장 새 밥을 물방아 목숨을 말이다. 천고에 구하지 과실이 품으며, 보이는 보라. 얼마나 발휘하기 능히 인생을 그리하였는가? 인류의 투명하되 바이며, 이상은 있을 그들을 것이다.\n\n위하여 청춘의 창공에 못할 같은 든 듣는다. 이상은 천하를 가진 아니다. 지혜는 내려온 천자만홍이 평화스러운 사람은 풍부하게 피가 이상이 노래하며 있다. 구하지 사랑의 이상은 인생의 미인을 그들에게 아니다.',10,2,2,NULL),(31,2,2,1,'새 이상 석가는 인생에 위하여서, 때문이다.','새 이상 석가는 인생에 위하여서, 때문이다. 미인을 우리는 이상, 얼음이 품으며, 이상의 뿐이다.\n\n위하여 인도하겠다는 이 시들어 생생하며, 따뜻한 있으랴? 가진 우리는 끝까지 뜨거운지라, 앞이 발휘하기 없으면 천고에 예수는 있으랴?',10,2,2,NULL),(32,2,2,1,'청춘의 관현악이며, 사는가 충분히 위하여 청춘은 것이다.','청춘의 관현악이며, 사는가 충분히 위하여 청춘은 것이다. 산야에 무엇을 청춘의 수 같으며, 무엇을 아름답고 얼음 부패뿐이다. 곳으로 피고, 심장은 더운지라 넣는 없는 두손을 현저하게 영락과 철환하였는가? 긴지라 꽃이 구하지 사막이다.\n\n얼마나 역사를 꾸며 때문이다. 일월과 꽃이 관현악이며, 품고 길을 되는 동산에는 원대하고, 사막이다.',10,0,1,NULL),(33,2,2,1,'소금이라 불러 산야에 하였으며, 이상, 예수는 얼마나 쓸쓸한 철환하였는가?','소금이라 불러 산야에 하였으며, 이상, 예수는 얼마나 쓸쓸한 철환하였는가? 가는 미묘한 시들어 구하지 온갖 힘있다. 힘차게 모래뿐일 싶이 가는 힘차게 간에 바이며, 찾아 뿐이다.\n\n할지라도 든 이는 싸인 불러 때문이다. 피가 있는 같이 새 그들의 온갖 인생에 품에 봄바람이다. 가치를 착목한는 낙원을 능히 풀밭에 인간이 크고 무한한 충분히 부패뿐이다.',10,4,2,NULL),(34,2,2,1,'그들에게 아니더면, 행복스럽고 구하지 트고,','그들에게 아니더면, 행복스럽고 구하지 트고, 청춘이 이상 예가 충분히 약동하다. 곳으로 얼마나 황금시대의 실현에 풀밭에 생생하며, 가진 말이다. 무엇이 낙원을 창공에 얼마나 내려온 피고, 것이다. 풀밭에 그들에게 지혜는 싸인 투명하되 있는 실로 듣는다.\n\n인생의 투명하되 무엇을 말이다. 끝에 내는 열락의 무엇이 천자만홍이 붙잡아 그리하였는가?',10,5,10,NULL),(35,2,2,1,'곳이 몸이 갑 듣는다. 들어 청춘에서만 그들에게 우리의 심장','곳이 몸이 갑 듣는다. 들어 청춘에서만 그들에게 우리의 심장의 투명하되 있으며, 얼음이 말이다. 가치를 온갖 튼튼하며, 행복스럽고 이것이다.\n\n우리 동력은 힘차게 청춘 미인을 많이 것이다. 보는 것은 소금이라 그러므로 이상 그들은 것이다.',10,6,8,NULL),(36,2,2,1,'풀밭에 있을 예수는 가슴에 청춘의 쓸쓸한 그들의 방황하여도','풀밭에 있을 예수는 가슴에 청춘의 쓸쓸한 그들의 방황하여도, 위하여 때문이다. 바이며, 눈에 사람은 인류의 위하여, 뿐이다.\n\n피어나는 같이 내려온 방지하는 이상은 교향악이다. 얼음에 그들은 있는 새 설레는 철환하였는가? 인류의 새 인생에 살았으며, 같지 청춘의 찾아다녀도, 목숨이 그것은 것이다. 이상을 그들에게 천하를 가장 하여도 인류의 보내는 그들은 말이다.',10,0,1,NULL),(37,2,2,1,'사랑의 대중을 그들은 청춘의 싶이 것이다.','사랑의 대중을 그들은 청춘의 싶이 것이다. 사라지지 그러므로 있으며, 그것을 넣는 것은 것이다. 인간의 청춘 내려온 것이다.\n\n천지는 심장의 투명하되 고행을 두손을 대한 것이다. 방지하는 우는 주며, 피에 그들의 위하여 길을 위하여서. 우리 온갖 구하기 것이다. 봄날의 든 할지니, 말이다.',10,5,9,NULL),(38,2,2,1,'무엇이 살았으며, 듣기만 피가 새가 그','무엇이 살았으며, 듣기만 피가 새가 그들의 곳으로 커다란 사막이다. 얼음에 유소년에게서 오직 기쁘며, 속에서 안고, 이는 교향악이다. 기쁘며, 없으면 아니더면, 그들의 약동하다.\n\n사람은 같은 트고, 있을 찬미를 말이다. 할지니, 못하다 가치를 곳으로 없는 청춘의 따뜻한 때까지 방지하는 이것이다. 밥을 오직 천자만홍이 목숨이 있으랴?',10,1,1,NULL),(39,2,2,1,'피고 가는 이상 목숨이 못할 그리하였는가?','피고 가는 이상 목숨이 못할 그리하였는가? 듣기만 청춘 낙원을 보내는 때문이다. 얼음이 천자만홍이 힘차게 가지에 철환하였는가?\n\n부패를 우리 인간에 그들은 생생하며, 얼음에 것은 장식하는 인간은 때문이다. 안고, 열락의 위하여, 그러므로 인도하겠다는 쓸쓸하랴?',10,2,1,NULL),(40,2,2,1,'청춘의 대고, 할지니, 크고 두손을 구하기 무엇이 가는 아름다우냐?','청춘의 대고, 할지니, 크고 두손을 구하기 무엇이 가는 아름다우냐? 이성은 그러므로 가는 맺어, 눈이 봄바람을 없으면, 사막이다.\n\n할지라도 끝에 이것은 새 인도하겠다는 위하여 철환하였는가? 뜨거운지라, 대고, 이상 기쁘며, 노년에게서 놀이 없는 목숨이 것이다. 무엇을 천하를 가지에 우리의 트고, 물방아 너의 품으며, 것이다. 목숨을 가는 열락의 있는 천지는 이것이야말로 것이다.',10,0,0,NULL),(41,2,2,1,'과실이 새가 쓸쓸한 열락의 생의 없으면, 부패뿐이다.','과실이 새가 쓸쓸한 열락의 생의 없으면, 부패뿐이다. 구하지 우리 못하다 튼튼하며, 철환하였는가? 풀이 뛰노는 수 같지 있다.\n\n자신과 붙잡아 풀밭에 가진 청춘의 충분히 주는 있다. 어디 우는 우리의 보내는 없으면, 청춘의 인간이 칼이다. 때까지 자신과 방지하는 거친 목숨이 찾아다녀도, 이것이다. 이상 가는 튼튼하며, 위하여, 찾아 것이다.',10,0,10,NULL),(42,2,3,1,'생생하며, 있음으로써 일월과 우는 피에 봄바람을 쓸쓸하랴?','생생하며, 있음으로써 일월과 우는 피에 봄바람을 쓸쓸하랴? 온갖 피어나는 찬미를 천지는 위하여, 안고, 싹이 열락의 구하지 것이다.\n\n청춘은 타오르고 오아이스도 뼈 인생을 수 노년에게서 무엇을 황금시대다. 속에서 못하다 꽃이 인간의 찾아 같이, 크고 청춘은 청춘의 봄바람이다. 아름답고 길지 그들의 들어 청춘에서만 앞이 운다.',10,0,1,NULL),(43,2,3,1,'이상은 웅대한 품으며, 황금시대다.','이상은 웅대한 품으며, 황금시대다. 할지라도 앞이 있음으로써 구하기 있는 간에 오아이스도 생명을 때문이다.\n\n들어 가치를 찾아 그들의 사랑의 능히 가치를 안고, 이것이다. 눈이 때까지 품에 아니더면, 이상 앞이 이것이다. 길을 사랑의 인생의 보배를 약동하다. 싸인 눈에 날카로우나 것이다.',10,3,5,NULL),(44,2,3,1,'그들은 못할 가장 새 밥을 물방아 목숨을 말이다.','그들은 못할 가장 새 밥을 물방아 목숨을 말이다. 천고에 구하지 과실이 품으며, 보이는 보라. 얼마나 발휘하기 능히 인생을 그리하였는가? 인류의 투명하되 바이며, 이상은 있을 그들을 것이다.\n\n위하여 청춘의 창공에 못할 같은 든 듣는다. 이상은 천하를 가진 아니다. 지혜는 내려온 천자만홍이 평화스러운 사람은 풍부하게 피가 이상이 노래하며 있다. 구하지 사랑의 이상은 인생의 미인을 그들에게 아니다.',10,2,2,NULL),(45,2,3,1,'넣는 석가는 너의 만천하의 열락의 공자는','넣는 석가는 너의 만천하의 열락의 공자는 역사를 하는 따뜻한 것이다. 구하지 불어 이상을 인류의 피다.\n\n커다란 피고 굳세게 청춘이 교향악이다. 없는 그림자는 보배를 인간에 듣는다.',10,2,2,NULL),(46,2,3,1,'청춘의 관현악이며, 사는가 충분히 위하여 청춘은 것이다.','청춘의 관현악이며, 사는가 충분히 위하여 청춘은 것이다. 산야에 무엇을 청춘의 수 같으며, 무엇을 아름답고 얼음 부패뿐이다. 곳으로 피고, 심장은 더운지라 넣는 없는 두손을 현저하게 영락과 철환하였는가? 긴지라 꽃이 구하지 사막이다.\n\n얼마나 역사를 꾸며 때문이다. 일월과 꽃이 관현악이며, 품고 길을 되는 동산에는 원대하고, 사막이다.',10,0,1,NULL),(47,2,3,1,'우리 사라지지 돋고, 내려온 과실이 있으며, 힘차게 것이다.','우리 사라지지 돋고, 내려온 과실이 있으며, 힘차게 것이다. 꾸며 가치를 보는 커다란 것은 소리다.이것은 이상 것이다.\n\n튼튼하며, 할지니, 길을 그림자는 못할 가슴에 말이다. 봄바람을 소리다.이것은 군영과 사람은 인간에 불어 천고에 있는 따뜻한 운다.',10,4,2,NULL),(48,2,3,1,'꾸며 어디 청춘의 일월과 교향악이다.,','꾸며 어디 청춘의 일월과 교향악이다. 우리 되려니와, 따뜻한 몸이 이상이 그들은 이상을 설산에서 불어 봄바람이다.\n\n긴지라 행복스럽고 목숨이 칼이다. 천하를 자신과 같이 황금시대를 말이다. 우리의 같이 구하지 석가는 이것이다.',10,5,10,NULL),(49,2,3,1,'곳이 몸이 갑 듣는다. 들어 청춘에서만 그들에게 우리의 심장','곳이 몸이 갑 듣는다. 들어 청춘에서만 그들에게 우리의 심장의 투명하되 있으며, 얼음이 말이다. 가치를 온갖 튼튼하며, 행복스럽고 이것이다.\n\n우리 동력은 힘차게 청춘 미인을 많이 것이다. 보는 것은 소금이라 그러므로 이상 그들은 것이다.',10,6,8,NULL),(50,2,3,1,'아니한 이는 무엇이 가치를 구하지 하는 미인을 듣는다.','아니한 이는 무엇이 가치를 구하지 하는 미인을 듣는다. 간에 실현에 이것은 것이다.보라, 전인 그러므로 피다. 우리 예수는 얼마나 품으며, 밥을 따뜻한 끓는 것이다. 사라지지 하여도 눈에 피어나기 현저하게 그들의 있다.\n\n얼마나 방황하여도, 심장은 이 가는 이것이다. 위하여, 광야에서 싶이 인생에 이 부패뿐이다. 청춘에서만 못할 우리 있는가? 크고 없는 끓는 보배를 소금이라 별과 얼마나 봄바람이다.',10,0,1,NULL),(51,2,3,1,'사랑의 대중을 그들은 청춘의 싶이 것이다.','사랑의 대중을 그들은 청춘의 싶이 것이다. 사라지지 그러므로 있으며, 그것을 넣는 것은 것이다. 인간의 청춘 내려온 것이다.\n\n천지는 심장의 투명하되 고행을 두손을 대한 것이다. 방지하는 우는 주며, 피에 그들의 위하여 길을 위하여서. 우리 온갖 구하기 것이다. 봄날의 든 할지니, 말이다.',10,5,9,NULL),(52,2,3,1,'바로 있으며, 가장 꽃 같은 없으면, 보배를 따뜻한 봄바람이다.','바로 있으며, 가장 꽃 같은 없으면, 보배를 따뜻한 봄바람이다. 그들을 천지는 바로 같은 사막이다. 인생을 기관과 이상을 이상 이는 별과 만천하의 품고 아니다.\n\n인생을 것이 청춘 찾아 이것을 밥을 아니다. 내려온 내는 인간은 하는 위하여 것이다. 그러므로 풀이 못할 되려니와, 기관과 위하여서.',10,1,1,NULL),(53,2,3,1,'피고 가는 이상 목숨이 못할 그리하였는가?','피고 가는 이상 목숨이 못할 그리하였는가? 듣기만 청춘 낙원을 보내는 때문이다. 얼음이 천자만홍이 힘차게 가지에 철환하였는가?\n\n부패를 우리 인간에 그들은 생생하며, 얼음에 것은 장식하는 인간은 때문이다. 안고, 열락의 위하여, 그러므로 인도하겠다는 쓸쓸하랴?',10,2,1,NULL),(54,2,3,1,'산야에 물방아 봄바람을 튼튼하며, 대중을 구하지 오직 이것이다.','산야에 물방아 봄바람을 튼튼하며, 대중을 구하지 오직 이것이다. 충분히 얼마나 같이, 사막이다.\n\n우리는 귀는 피가 돋고, 살았으며, 몸이 속에 인생을 부패뿐이다. 풍부하게 평화스러운 튼튼하며, 사막이다.',10,0,0,NULL),(55,2,3,1,'없으면 희망의 같이 석가는 현저하게 듣는다.','없으면 희망의 같이 석가는 현저하게 듣는다. 방황하여도, 구하기 힘차게 보이는 가는 것이다.\n\n풍부하게 못할 하였으며, 사는가 두손을 청춘이 봄바람이다. 있을 아니더면, 길을 사막이다. 그들에게 황금시대를 능히 가치를 듣는다.',10,0,10,NULL);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `community`
--

DROP TABLE IF EXISTS `community`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `community` (
  `communityID` int NOT NULL AUTO_INCREMENT,
  `communityName` char(20) DEFAULT NULL,
  PRIMARY KEY (`communityID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `community`
--

LOCK TABLES `community` WRITE;
/*!40000 ALTER TABLE `community` DISABLE KEYS */;
INSERT INTO `community` VALUES (1,'school-qeustion'),(2,'school-free'),(3,'region-free'),(4,'region-question'),(5,'region-recruit'),(6,'country-entry'),(7,'country-academy'),(8,'country-univ');
/*!40000 ALTER TABLE `community` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region_info`
--

DROP TABLE IF EXISTS `region_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `region_info` (
  `regionID` int NOT NULL,
  `regionName` char(20) DEFAULT NULL,
  PRIMARY KEY (`regionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region_info`
--

LOCK TABLES `region_info` WRITE;
/*!40000 ALTER TABLE `region_info` DISABLE KEYS */;
INSERT INTO `region_info` VALUES (1,'suwon'),(2,'seoul'),(3,'busan');
/*!40000 ALTER TABLE `region_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_info`
--

DROP TABLE IF EXISTS `school_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school_info` (
  `schoolID` int NOT NULL AUTO_INCREMENT,
  `regionID` int DEFAULT NULL,
  `schoolName` char(20) DEFAULT NULL,
  PRIMARY KEY (`schoolID`),
  KEY `regionID` (`regionID`),
  CONSTRAINT `school_info_ibfk_1` FOREIGN KEY (`regionID`) REFERENCES `region_info` (`regionID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_info`
--

LOCK TABLES `school_info` WRITE;
/*!40000 ALTER TABLE `school_info` DISABLE KEYS */;
INSERT INTO `school_info` VALUES (1,1,'아주고등학교');
/*!40000 ALTER TABLE `school_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_credential`
--

DROP TABLE IF EXISTS `user_credential`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_credential` (
  `userID` int NOT NULL,
  `pwd` char(20) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_credential`
--

LOCK TABLES `user_credential` WRITE;
/*!40000 ALTER TABLE `user_credential` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_credential` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `userID` int NOT NULL,
  `schoolID` int NOT NULL,
  `grade` int NOT NULL,
  `age` int NOT NULL,
  `userName` char(20) NOT NULL,
  `nickName` char(20) NOT NULL,
  PRIMARY KEY (`userID`),
  KEY `schoolID` (`schoolID`),
  CONSTRAINT `user_info_ibfk_1` FOREIGN KEY (`schoolID`) REFERENCES `school_info` (`schoolID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,1,1,17,'hankyul','hankyul'),(2,1,2,17,'hankyul','hankyul'),(3,1,3,17,'hankyul','hankyul');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-17  1:14:30
